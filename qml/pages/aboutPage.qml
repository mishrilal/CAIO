import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15

Item {
    id: item1
    Rectangle {
        id: rectangle
        color: "#16181d"
        anchors.fill: parent
        Rectangle{
            width: 448
            height: 302
            color: "#00000000"
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter

            Label {
                id: label
                x: 284
                color: "#ffffff"
                text: qsTr("CAIO")
                anchors.top: iconApp.bottom
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                font.pointSize: 26
                font.family: "Times New Roman"
                font.bold: true
                anchors.topMargin: 10
                anchors.horizontalCenter: parent.horizontalCenter
            }

            Text {
                id: text1
                x: 307
                width: 169
                color: "#ffffff"
                text: {
                    "<i>Version </i><b>0.1.45</b>"
                }
                anchors.top: label.bottom
                anchors.bottom: parent.bottom
                font.pixelSize: 18
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignTop
                anchors.bottomMargin: 273
                font.family: "Times New Roman"
                anchors.topMargin: 20
                anchors.horizontalCenter: parent.horizontalCenter

            }

            Image {
                id: iconApp
                x: 270
                y: 20
                width: 100
                height: 100
                anchors.top: parent.top
                source: "../../images/svg_images/logo_icon.svg"
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.topMargin: 20
                fillMode: Image.PreserveAspectFit
            }

            ColorOverlay{
                anchors.fill: iconApp
                source: iconApp
                color: "#ffffff"
            }

        }




    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
