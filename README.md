# JitsiMeet
JitsiMeet integrate with Django

Integration

To enable the Jitsi Meet API in your application you must use one 
of the following JavaScript (JS) Jitsi Meet API library scripts and integrate it into your application:


meet.jit.si:
<script src='https://meet.jit.si/external_api.js'></script>

Creating the Jitsi Meet API object 
For example:

const domain = 'meet.jit.si';
const options = {
    roomName: 'JitsiMeetAPIExample',
    width: 700,
    height: 700,
    parentNode: document.querySelector('#meet')
};
const api = new JitsiMeetExternalAPI(domain, options);

Please Check Jitsi Official Docx.

https://jitsi.github.io/handbook/docs/dev-guide/dev-guide-iframe
