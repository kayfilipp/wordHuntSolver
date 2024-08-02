import streamlit as st
from libs import grid
st.header("WordHunt Solver")
st.session_state['grid_dim'] = 3


def reset():
    del st.session_state['grid']


def main():
    if not st.session_state.get('grid'):
        st.subheader("Please edit the word grid and press continue.", divider='rainbow')
        st.data_editor(grid.create_grid(st.session_state['grid_dim']), key="temp_grid")
        st.button("Continue", on_click=grid.submit_word_grid, args=[st])
        return

    grid.render_table(st)
    st.button("Reset", on_click=reset)

    st.write("Solution:")


main()