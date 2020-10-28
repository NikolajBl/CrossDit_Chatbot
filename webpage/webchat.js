import { Widget } from 'rasa-webchat';
class WebChat extends React.Component {
    loadChatbot() {
    return (
        <Widget
        initPayload={"/get_started"}
        socketUrl={"http://localhost:5500"}
        hideWhenNotConnected={false}
        socketPath={"/socket.io/"}
        customData={{"language": "en"}} // arbitrary custom data. Stay minimal as this will be added to the socket
        title={"Title"}
        />
    )
    }

    render() {
        return (
        <div>
            {this.loadChatbot()}	 
        </div>
        )
    }
}
WebChat.render()