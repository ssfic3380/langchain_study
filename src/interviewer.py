from interviewer_chain_builder import InterviewerChainBuilder

class Interviewer:
    def __init__(self, company_name, job_name, job_posting, cover_letter):
        self.company_name = company_name
        self.job_name = job_name
        self.job_posting = job_posting
        self.cover_letter = cover_letter

        self.chain = InterviewerChainBuilder(company_name, job_name, job_posting, cover_letter).get_full_chain()

    def analyze_cover_letter(self):
        input = f"""
        {self.company_name}의 {self.job_name} 포지션을 뽑는 면접관의 입장에서, 지원자의 자기소개서를 평가해봅시다.
        좋았던 부분과 개선이 필요한 부분을 구분하여 평가하세요.
        아래와 같은 형식으로 답변을 제공하세요.
        ```
        좋은 점:
         - Strengths of the applicant
            
        아쉬운 점:
         - Areas for improvement
        ```
        """
        return self.chain.run(input)

    def generate_interview_questions(self, n):
        input = f"""
        당신은 {self.company_name} 회사의 면접관으로서, {self.job_name} 포지션에 지원한 지원자를 대상으로 면접 질문을 준비하고 있습니다.
        지원자의 자기소개서와 회사의 모집 공고를 바탕으로, 지원자의 적합성을 판단할 수 있는 면접 질문 {n}개를 만들어보십시오.
        이 질문들은 지원자의 기술, 경험, 그리고 문화 적합성에 대해 탐구하는 데 도움이 되어야 합니다.
        각 질문은 'Qn. 질문 내용' 형식으로 출력해주십시오.
        예시 출력 형식:
        ```
        Q1. 질문 내용
        Q2. 질문 내용
        Q3. 질문 내용
        Q4. 질문 내용
        Q5. 질문 내용
        ```
        """
        return self.chain.run(input)

    def analyze_interview_answer(self, question, answer):
        input = f"""
        당신은 {self.company_name}라는 회사의 면접관으로서, {self.job_name} 포지션에 지원한 지원자의 답변을 평가하고 있습니다. 아래 제공된 질문과 답변을 바탕으로 분석하십시오. 
        지원자의 답변에 대한 평가는 잘한 점과 개선해야할 점으로 나눠서 제공하며, 질문이 지식 확인을 위한 것인지, 경험 확인을 위한 것인지를 분류하십시오. 
        잘한 점이나 아쉬운 점이 없을 경우, 그렇다고 명시하십시오.
        
        질문: {question}
        답변: {answer}
        
        분석하고 평가한 내용을 다음 형식에 맞추어 출력하십시오. []는 당신이 내용을 채워 넣어야 하는 곳입니다.
        ```
        질문 분류:
        [Question Classification]
        
        잘한 점:
        [Positive Aspects]
        
        아쉬운 점:
        [Areas for Improvement]
        ```
        """
        return self.chain.run(input)

    def generate_follow_up_question(self, question, answer):
        input = f"""
        당신은 {self.company_name}라는 회사의 면접관으로서, {self.job_name} 포지션에 지원한 지원자의 답변을 보고 후속 질문을 만들고 있습니다.
        후속 질문 1개를 준비하되, 후속 질문이 필요 없다면 그런 사실을 명시하십시오.
        
        질문: {question}
        답변: {answer}
        
        후속 질문을 다음 형식에 맞추어 출력하십시오.
        ```
        후속 질문: [Follow-up queestion]
        ```
        """
        return self.chain.run(input)

    def analyze_interview_answer_and_generate_follow_up_question(self, question, answer):
        input = f"""
        당신은 {self.company_name}라는 회사의 면접관으로서, {self.job_name} 포지션에 지원한 지원자의 답변을 분석하고 평가하고 있습니다. 아래 제공된 질문과 답변을 바탕으로 분석하십시오. 
        지원자의 답변에 대한 평가는 잘한 점과 개선해야 할 점으로 나눠서 제공하며, 질문이 지식 확인을 위한 것인지, 경험 확인을 위한 것인지를 분류하십시오. 
        잘한 점이나 아쉬운 점이 없을 경우, 그렇다고 명시하십시오. 그리고 분석한 결과를 바탕으로 후속 질문 1개를 준비하십시오. 후속 질문이 필요 없다면 그런 사실을 명시하십시오.
        
        질문: {question}
        답변: {answer}
        
        분석하고 평가한 내용과 후속 질문을 다음 형식에 맞추어 출력하십시오. []는 당신이 내용을 채워 넣어야 하는 곳입니다.
        ```
        질문 분류:
        [Question Classification]
        
        잘한 점:
        [Positive Aspects]
        
        아쉬운 점:
        [Areas for Improvement]
        
        후속 질문: [Follow-up question]
        ```
        """
        return self.chain.run(input)

    def analyze_interview_answer_and_generate_follow_up_question_with_guideline(self, question, answer):
        input = f"""
        당신은 {self.company_name}라는 회사의 면접관으로서, {self.job_name} 포지션에 지원한 지원자의 답변을 분석하고 평가하고 있습니다. 아래 제공된 질문과 답변을 바탕으로 분석하십시오. 

        지원자의 답변에 대한 평가는 잘한 점과 개선해야 할 점으로 나눠서 제공하며, 질문이 지식 확인을 위한 것인지, 경험 확인을 위한 것인지를 분류하십시오. 
        잘한 점이나 아쉬운 점이 없을 경우, 그렇다고 명시하십시오. 
        
        그리고 분석한 결과를 바탕으로 후속 질문을 준비하십시오. 질문 분류가 '지식'인 경우, 지원자가 핵심적인 내용을 충분히 이해하고 있는지 확인하는 후속 질문을 준비해야 합니다. 만약 지원자가 답변에서 중요한 내용을 빠트렸다면, 그 부분에 대해 물어봅니다.
        
        질문 분류가 '경험'인 경우, 지원자가 실제로 해당 경험을 가지고 있는지 확인하는 후속 질문을 준비해야 합니다. 만약 지원자가 경험에 대해 구체적으로 설명하지 않았다면, 그 경험에 대한 자세한 설명을 요청하는 질문을 합니다. 특히 그 경험이 직무 관련 경험이거나 협업과 관련된 경험이라면, 지원자의 역할과 배운 점에 대해 물어봅니다.
        
        후속 질문이 필요 없다면 그런 사실을 명시하십시오.
        
        질문: {question}
        답변: {answer}
        
        분석하고 평가한 내용과 후속 질문을 다음 형식에 맞추어 출력하십시오. []는 당신이 내용을 채워 넣어야 하는 곳입니다.
        ```
        질문 분류:
        [Question Classification]
        
        잘한 점:
        [Positive Aspects]
        
        아쉬운 점:
        [Areas for Improvement]
        
        후속 질문: [Follow-up question]
        ```
        """
        return self.chain.run(input)