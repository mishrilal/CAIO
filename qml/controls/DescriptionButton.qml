import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15

Button{
    id: btnDescriptionBar
    text: qsTr("About")
    //Custom properties
    property color btnColorDefault: "#1c1d20"
    property color btnColorMouseOver: "#23272E"
    property color btnColorClicked: "#00a1f1"
    width: 50
    height: 25




    QtObject{
        id: internal

        // Mouse Hover and Click Change Color
        property var dynamicColor: if(btnDescriptionBar.down){
                                       btnDescriptionBar.down ? btnColorClicked : btnColorDefault
                                   } else {
                                       btnDescriptionBar.hovered ? btnColorMouseOver : btnColorDefault
                                   }
    }


    background: Rectangle{
        id: bgBtn
        color: internal.dynamicColor

    }

    contentItem: Item {
        anchors.fill: parent
        id: content

        Text{
            color: "#ffffff"
            text: btnDescriptionBar.text
            anchors.fill: parent
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            wrapMode: Text.WordWrap
            font: btnDescriptionBar.font

        }
    }

}
