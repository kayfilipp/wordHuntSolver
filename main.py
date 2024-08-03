import streamlit as st
from libs import grid
from classes import Nodes

st.set_page_config(
    page_title="WordHunt Solver App"
)
st.header("WordHunt Solver")
st.caption("A Project by Luke Mileski & Filipp Kay")
# st.session_state['grid_dim'] = 3


def reset():
    del st.session_state['grid']
    del st.session_state['results']
    del st.session_state['grid_final']
    del st.session_state['grid_dim']


def init_dim():
    st.session_state['grid_dim'] = st.session_state['grid_dim_tmp']
    return


def main():

    if not st.session_state.get('grid_dim', None):
        st.number_input("Please enter the number of rows and columns.", key="grid_dim_tmp", format='%d', min_value=2)
        st.button("Submit", on_click=init_dim)
        return

    if not st.session_state.get('grid'):
        st.subheader("Please edit the word grid and press continue.", divider='rainbow')
        st.data_editor(grid.create_grid(st.session_state['grid_dim']), key="temp_grid")
        st.button("Continue", on_click=grid.submit_word_grid, args=[st])
        return

    if not st.session_state.get('grid_final', None):
        print("transforming grid...")
        grid.transform_grid(st)

    # if not st.session_state.get('colored_grid', None):
    #     grid.render_table(st)
    # else:
    #     grid.render_colored_table(st)

    # st.button("Reset", on_click=reset)
    # st.write("Words:")

    if not st.session_state.get('results', None):
        game = Nodes.Game()
        game.find_words(st.session_state['grid_final'])
        st.session_state['results'] = set([])

        longest_word = []

        for results in game.all_search_results:
            if len(longest_word) < len(results.longest_word):
                longest_word = results.longest_word
            st.session_state['results'] = st.session_state['results'] | results.words_by_character

        st.session_state['longest_word'] = longest_word

    grid.render_colored_table(st)
    st.button("Reset", on_click=reset)
    st.write("Words:")
    st.text(st.session_state['results'])


main()
