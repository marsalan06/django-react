import React , {Component} from "react";
import CreateRoomPage from "./CreateRoomPage";
import RoomJoinPage from "./RoomJoinPage";
import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link,
    Redirect,
} from "react-router-dom";

export default class HomePage extends Component{
    constructor(props){
        super(props);
    }
    render(){
        // return <p>This is the home page</p>
        return <Router>
            <Routes>
                <Route path='/home' element={<Home />}></Route>
                <Route path='/join' element={<RoomJoinPage/>}></Route>
                <Route path='/create' element={<CreateRoomPage/>}/>
            </Routes>
        </Router>
    }
}

function Home(){
    return(
        <div>
            <h1>This is the home Page</h1>
        </div>
    )
}