import streamlit as st
import chess

# Set page configuration
st.set_page_config(
    page_title="My Chess Arena",
    page_icon="♔",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark theme styling matching the image
st.markdown("""
<style>
    /* Dark theme background */
    .stApp {
        background-color: #0e1117;
    }
    
    /* Main header styling */
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 0.8rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 1.5rem;
        box-shadow: 0 3px 12px rgba(0,0,0,0.3);
        position: relative;
    }
    
    .header-icon {
        position: absolute;
        left: 18px;
        top: 50%;
        transform: translateY(-50%);
        font-size: 1.6rem;
        color: #a855f7;
    }
    
    .header-title {
        font-size: 1.6rem;
        font-weight: bold;
        margin: 0;
    }
    
    /* Chess board container */
    .board-container {
        max-width: 400px;
        margin: 0 auto;
        padding: 0.8rem;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }
    
    /* Coordinate labels */
    .coordinate-label {
        color: #ffffff;
        font-weight: bold;
        font-size: 0.9rem;
        text-align: center;
        padding: 0.2rem;
    }
    
    .rank-label {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 20px;
        height: 40px;
    }
    
    .file-label {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 20px;
        width: 40px;
    }
    
    /* Chess square styling */
    .chess-square {
        border: 1px solid #374151;
        transition: all 0.2s ease;
        aspect-ratio: 1;
    }
    
    .chess-square:hover {
        transform: scale(1.02);
        box-shadow: 0 2px 8px rgba(0,0,0,0.3);
    }
    
    /* Game controls */
    .game-controls {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 0.7rem;
        border-radius: 8px;
        color: white;
        margin: 0.7rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: bold;
        font-size: 0.9rem;
        transition: all 0.3s ease;
        margin: 0.3rem 0;
    }
    
    .stButton > button:hover {
        background: linear-gradient(45deg, #764ba2, #667eea);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    
    /* Status messages */
    .status-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 0.6rem;
        border-radius: 6px;
        color: white;
        margin: 0.4rem 0;
        box-shadow: 0 1px 6px rgba(0,0,0,0.2);
    }
    
    .game-status {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        padding: 0.6rem;
        border-radius: 6px;
        color: white;
        text-align: center;
        margin: 0.4rem 0;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }
    
    /* Move history */
    .move-history {
        background: rgba(255, 255, 255, 0.1);
        padding: 0.7rem;
        border-radius: 6px;
        border-left: 2px solid #667eea;
        color: white;
        margin: 0.7rem 0;
    }
    
    /* Input field styling */
    .input-container {
        background: rgba(255, 255, 255, 0.1);
        padding: 0.7rem;
        border-radius: 6px;
        margin: 0.7rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Unicode symbols for chess pieces
PIECES = {
    "P": "♙", "N": "♘", "B": "♗", "R": "♖", "Q": "♕", "K": "♔",
    "p": "♟", "n": "♞", "b": "♝", "r": "♜", "q": "♛", "k": "♚", None: ""
}

def rerun():
    """Rerun the Streamlit app"""
    st.rerun()

def render_chess_board(board, selected_square=None, legal_moves=[], last_move=None):
    """Render the chess board with coordinates and dark theme"""
    
    # Create the board container
    st.markdown('<div class="board-container">', unsafe_allow_html=True)
    
    # File labels (a-h) at the bottom
    file_cols = st.columns(8)
    for i, col in enumerate(file_cols):
        with col:
            st.markdown(f'<div class="coordinate-label file-label">{chr(97 + i)}</div>', unsafe_allow_html=True)
    
    # Render the chess board with rank labels
    for rank in range(8):
        cols = st.columns([0.5, 8, 0.5])  # Rank label, board squares, rank label
        
        with cols[0]:
            st.markdown(f'<div class="coordinate-label rank-label">{8 - rank}</div>', unsafe_allow_html=True)
        
        with cols[1]:
            board_cols = st.columns(8)
            for file in range(8):
                sq = chess.square(file, 7 - rank)
                piece = board.piece_at(sq)
                label = PIECES[piece.symbol()] if piece else " "
                
                # Determine square colors
                if selected_square == sq:
                    # Selected square - bright yellow
                    bg_color = "#FFD700"
                    text_color = "#000000"
                elif sq in legal_moves:
                    # Legal moves - light green
                    bg_color = "#90EE90"
                    text_color = "#000000"
                elif last_move and (sq == last_move.from_square or sq == last_move.to_square):
                    # Last move - light blue
                    bg_color = "#87CEEB"
                    text_color = "#000000"
                else:
                    # Regular squares - alternating colors
                    if (rank + file) % 2 == 0:
                        bg_color = "#F0D9B5"  # Light square
                        text_color = "#000000"
                    else:
                        bg_color = "#B58863"  # Dark square
                        text_color = "#FFFFFF"
                
                # Create button styling
                button_style = f"""
                <style>
                div[data-testid="stButton"] button[kind="secondary"] {{
                    background-color: {bg_color} !important;
                    color: {text_color} !important;
                    border: 1px solid #374151 !important;
                    border-radius: 4px !important;
                    font-size: clamp(1.2rem, 3vw, 1.8rem) !important;
                    font-weight: bold !important;
                    width: 100% !important;
                    height: clamp(35px, 4vw, 50px) !important;
                    min-height: 35px !important;
                    max-height: 50px !important;
                    transition: all 0.2s ease !important;
                    margin: 0px !important;
                    aspect-ratio: 1 !important;
                    padding: 0px !important;
                }}
                div[data-testid="stButton"] button[kind="secondary"]:hover {{
                    transform: scale(1.02) !important;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.3) !important;
                }}
                </style>
                """
                st.markdown(button_style, unsafe_allow_html=True)
                
                # Create the button
                if board_cols[file].button(
                    label, 
                    key=f"chess_sq_{rank}_{file}", 
                    help=f"Square: {chess.square_name(sq)}", 
                    use_container_width=True,
                    type="secondary"
                ):
                    st.markdown('</div>', unsafe_allow_html=True)
                    return sq
        
        with cols[2]:
            st.markdown(f'<div class="coordinate-label rank-label">{8 - rank}</div>', unsafe_allow_html=True)
    
    # File labels (a-h) at the top
    file_cols = st.columns(8)
    for i, col in enumerate(file_cols):
        with col:
            st.markdown(f'<div class="coordinate-label file-label">{chr(97 + i)}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    return None

def main():
    """Main function to run the chess game"""
    
    # Header matching the image design
    st.markdown("""
    <div class="main-header">
        <div class="header-icon">♔</div>
        <h1 class="header-title">My Chess Arena</h1>
    </div>
    """, unsafe_allow_html=True)

    # Initialize session state
    if "board" not in st.session_state:
        st.session_state.board = chess.Board()
        st.session_state.selected = None
        st.session_state.last_move = None
        st.session_state.invalid_move = False
        st.session_state.game_over = False

    board = st.session_state.board
    selected = st.session_state.selected
    last_move = st.session_state.last_move
    invalid_move = st.session_state.get("invalid_move", False)

    # Create two columns for layout
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Game status
        turn_color = "White" if board.turn else "Black"
        st.markdown(f"""
        <div class="status-box">
            <h3>🎯 Current Turn: {turn_color}</h3>
            <p>Click on a piece to select it, then click on a destination square to move.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Render the chess board
        clicked_square = render_chess_board(board, selected, [], last_move)

    with col2:
        # Game controls
        st.markdown("""
        <div class="game-controls">
            <h3>🎮 Game Controls</h3>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔄 Reset Board", use_container_width=True):
            st.session_state.board = chess.Board()
            st.session_state.selected = None
            st.session_state.last_move = None
            st.session_state.invalid_move = False
            st.session_state.game_over = False
            rerun()
        
        if st.button("↩️ Undo Last Move", use_container_width=True):
            if len(board.move_stack) > 0:
                board.pop()
                st.session_state.selected = None
                st.session_state.last_move = None
                st.session_state.invalid_move = False
                st.session_state.game_over = False
                rerun()
        
        # Game status messages
        if board.is_checkmate():
            winner = "White" if not board.turn else "Black"
            st.markdown(f"""
            <div class="game-status">
                <h3>🏆 Checkmate!</h3>
                <p>{winner} wins the game!</p>
            </div>
            """, unsafe_allow_html=True)
            st.session_state.game_over = True
        elif board.is_stalemate():
            st.markdown("""
            <div class="game-status">
                <h3>🤝 Stalemate!</h3>
                <p>The game is a draw!</p>
            </div>
            """, unsafe_allow_html=True)
            st.session_state.game_over = True
        elif board.is_check():
            st.markdown("""
            <div class="game-status">
                <h3>⚠️ Check!</h3>
                <p>Your king is in danger!</p>
            </div>
            """, unsafe_allow_html=True)

        if invalid_move:
            st.markdown("""
            <div class="game-status">
                <h3>❌ Invalid Move!</h3>
                <p>Please select a valid piece and destination.</p>
            </div>
            """, unsafe_allow_html=True)

    # Handle square clicks
    if clicked_square is not None and not st.session_state.get("game_over", False):
        legal_moves = []
        if selected is not None:
            piece = board.piece_at(selected)
            if piece and ((piece.color and board.turn) or (not piece.color and not board.turn)):
                legal_moves = [move.to_square for move in board.legal_moves if move.from_square == selected]
        
        if selected is not None and clicked_square in legal_moves:
            # Make the move
            move = chess.Move(selected, clicked_square)
            board.push(move)
            st.session_state.last_move = move
            st.session_state.selected = None
            st.session_state.invalid_move = False
            rerun()
        elif board.piece_at(clicked_square) and ((board.piece_at(clicked_square).color and board.turn) or (not board.piece_at(clicked_square).color and not board.turn)):
            # Select a piece
            st.session_state.selected = clicked_square
            st.session_state.invalid_move = False
            rerun()
        else:
            # Invalid selection
            st.session_state.selected = None
            st.session_state.invalid_move = True
            rerun()

    # Move history
    st.markdown("### 📜 Move History")
    moves = list(board.move_stack)
    if moves:
        move_texts = []
        temp_board = chess.Board()
        
        for move in moves:
            try:
                move_texts.append(temp_board.san(move))
                temp_board.push(move)
            except:
                move_texts.append("...")
        
        # Display moves in a nice format
        move_history_html = '<div class="move-history">'
        for i in range(0, len(move_texts), 2):
            move_num = i // 2 + 1
            white_move = move_texts[i]
            black_move = move_texts[i + 1] if i + 1 < len(move_texts) else ""
            
            move_history_html += f'<div style="margin: 8px 0; padding: 8px; background: {"rgba(255,255,255,0.1)" if move_num % 2 == 0 else "rgba(255,255,255,0.05)"}; border-radius: 8px; font-weight: bold; color: white;">'
            move_history_html += f'<strong>{move_num}.</strong> {white_move} {black_move}'
            move_history_html += '</div>'
        
        move_history_html += '</div>'
        st.markdown(move_history_html, unsafe_allow_html=True)
    else:
        st.markdown('<div class="move-history"><p>No moves yet. Make the first move!</p></div>', unsafe_allow_html=True)

    # Input field at the bottom (matching the image)
    st.markdown("### 💬 Game Chat")
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    user_input = st.text_input("Enter your message or move notation:", placeholder="Type here...")
    if st.button("Send", use_container_width=True):
        if user_input:
            st.success(f"Message sent: {user_input}")
    st.markdown('</div>', unsafe_allow_html=True)

    # Instructions
    st.markdown("### 📖 How to Play")
    st.markdown("""
    - **Select a piece**: Click on any piece of your color (White goes first)
    - **Make a move**: Click on a destination square to move your selected piece
    - **Valid moves**: Only legal chess moves are allowed
    - **Game controls**: Use the buttons on the right to reset or undo moves
    - **Game status**: Watch for check, checkmate, and stalemate notifications
    """)

if __name__ == "__main__":
    main() 