def extract_memory(message:str) -> dict:

    memory = {}

    text = message.lower()

    #experincelevel

    if "fresher" in text:
        memory["experience_level"] = "Fresher"
    
    #skilss
    skills=[]

    if "python" in text:
        skills.append("Python")
    if "java" in text:
        skills.append("Java")
    if "javascript" in text:
        skills.append("JavaScript")
    if "c++" in text:           
        skills.append("C++")
    if "sql" in text:   
        skills.append("SQL")
    if "html" in text:
        skills.append("HTML")       
    if "css" in text:
        skills.append("CSS")
    if "react" in text:
        skills.append("React")
    if "angular" in text:
        skills.append("Angular")
    if "node.js" in text:
        skills.append("Node.js")        
    if skills:
        memory["skills"] = skills
    return memory
