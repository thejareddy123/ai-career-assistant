active_session =set()  # Set to store active session IDs


def create_session(session_id:str):
    """
    create a new session.
    """

    active_session.add(session_id)

def session_exists(session_id:str):
    """
    check if a session exists.
    """
    return session_id in active_session


