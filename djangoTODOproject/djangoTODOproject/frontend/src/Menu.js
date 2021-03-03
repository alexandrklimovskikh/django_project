import React, {Component} from 'react';
import './Menu.css';

class Menu extends Component {
    render() {
        return (
            <div id="menu-box">
                <ul class='main-menu'>
                    <li><a href='http://127.0.0.1:8000/api/users/'>Users</a></li>
                    <li><a href='http://127.0.0.1:8000/api'>API</a></li>
                </ul>
            </div>
        )
    }
}

export default Menu;