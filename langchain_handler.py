# langchain_handler.py
import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain.memory import ConversationBufferMemory
from web_search import WebSearch
from langsmith import traceable

class LangchainHandler:
    def __init__(self):
        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            api_key=os.getenv("GROQ_API_KEY"),
            temperature=1,
            max_tokens=150,
            streaming=True
        )
        self.memory = ConversationBufferMemory(
            return_messages=True,
            memory_key="chat_history"
        )
        self.web_search = WebSearch()

    @traceable
    def process_input(self, user_input, user_id, use_web_search=False):
        # Get search results if the toggle is enabled
        search_results = ""
        if use_web_search:
            search_results = self.web_search.search(user_input)

        # Get chat history
        chat_history = self.memory.load_memory_variables({})
        history_msgs = chat_history.get("chat_history", [])

        # Construct messages with context
        system_content = (
            """
            You are an intelligent assistant with access to the latest information.

            Primary Objectives:

                Accurate Information:
                    If you don't know the answer, simply say "I don't know"—do not fabricate responses.

                Conciseness:
                    Keep your answers brief, using no more than two sentences.

                Conversational Style:
                    Use a human-like, conversational tone to ensure natural dialogue flow.

                Comprehensive Integration:
                    Synthesize all provided search results to create a unified, cohesive summary.
                    Avoid relying on a single source; instead, combine information from multiple sources to provide a well-rounded answer.

                Formatting Restrictions:
                    No Quotes: Do not include any quoted text.
                    No Explanations: Do not explain your reasoning or process.
                    No Prompts: Do not mention or refer to prompts.
                    No Self-reference: Do not refer to yourself as an assistant or mention your capabilities.
                    No Apologies: Do not apologize.
                    No Filler: Avoid filler words or unnecessary content.
                    No Bullet Points: Present information in narrative form only.
                    Just Answer: Provide only the summary without additional text or commentary.

            Advanced Note Creation:

                Highlight Key Terms: Enclose essential vocabulary terms and key concepts with asterisks (e.g., term).
                Focus on Essentials: Eliminate any extraneous language, concentrating solely on the critical aspects of the topic.
                Source-Based: Base your notes strictly on the provided search results without adding any external information.
                Fallback on Knowledge: If recent search results lack detail, rely on your general knowledge.

            Instructions Summary:

                Do not include: Quotes, explanations, prompts, self-references, apologies, filler words, bullet points, or unnecessary elements.
                Provide only: A concise, integrated summary based on all provided search results, highlighting key terms as specified.

            Example Application:

            Given the following web search results about Moldova's presidential election:

                Candidate Overview: Pro-EU incumbent Maia Sandu vs. pro-Russian Alexandr Stoianoglo.
                Election Observers: International observers to present preliminary conclusions post-election.
                Historical Context: Impact of the Soviet Union's collapse on current politics.
                Election Challenges: Both candidates face significant burdens and threats.
                Voter Sentiment: Concerns over voter fraud and Russian influence.
                Election Day Events: Citizens voting amidst tensions and preparations.

            Your summarized notes would be:

            Moldova's presidential runoff features pro-EU incumbent Maia Sandu against pro-Russian Alexandr Stoianoglo, reflecting the nation's ongoing struggle between European integration and Russian influence. International observers are set to present their preliminary conclusions following the election, highlighting concerns over voter fraud and potential Russian disruptive activities. The election takes place in a context shaped by the Soviet Union's collapse, which continues to influence Moldova's political landscape. Both candidates face significant challenges, with Sandu addressing the burden of European aspirations and Stoianoglo navigating pro-Russian support. Citizens are voting amidst heightened tensions and rigorous preparations to ensure electoral integrity.
            """
            f"Recent search results: {search_results}\n\n" if search_results else
            "You are a helpful assistant. "
            "If you don't know the answer, simply say you don't know—do not fabricate responses. "
            "Keep your answers concise, using no more than three sentences. "
            "Respond in a human-like, and conversational style, ensuring the dialogue flows naturally.\n"
        )

        messages = [
            SystemMessage(content=system_content),
            *history_msgs,
            HumanMessage(content=user_input)
        ]

        # Stream response
        response_content = ""
        for chunk in self.llm.stream(messages):
            if chunk.content:
                response_content += chunk.content
                yield chunk

        # Save to memory after complete response
        self.memory.save_context(
            {"input": user_input},
            {"output": response_content}
        )
