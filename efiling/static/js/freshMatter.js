function enable(enabled) {
    var file1 = document.getElementById("urgencyFile");

    if (enabled) {
        file1.removeAttribute('disabled');
    } else {
        file1.setAttribute('disabled', 'disabled');
    }
}


document.querySelector('#TypeSelect').addEventListener("click", function (e) {
    var e = document.getElementById("TypeSelect");
    var value = e.options[e.selectedIndex].text;

    if (value == "Civil") {
        document.querySelector("#CaseType").innerHTML = `
       <option value="select" disabled>Select</option>
        <optgroup label="-------CIVIL-------">
            <option value="AO">AO-APPEAL FROM ORDER</option>
            <option value="CA">CA-CIVIL APPLICATION</option>
            <option value="CR">CR-CIVIL REFERENCES</option>
            <option value="CRA">CRA-CIVIL REVISION APPLICATION</option>
            <option value="FA">FA-FIRST APPEAL</option>
            <option value="LPA">LPA-LETTERS PATENT APPEAL</option>
            <option value="MCA">MCA-MISC. CIVIL APPLICATION</option>
            <option value="MCACP">MCACP-MISC. CIVIL APPLN. (CONTEMPT PETITION)</option>
            <option value="SA">SA-SECOND APPEAL</option>
            <option value="SCA">SCA-SPECIAL CIVIL APPLICATION</option>
            <option value="X-OBJ">X-OBJ-CROSS OBJECTION</option>
            <option value="WPPIL">WPPIL-WRIT PETITION (PIL)</option>
            <option value="CPTA">CPTA-APPEAL IN CONTEMPT PROCEEDINGS</option>
            <option value="AS">AS-ADMIRALITY SUIT</option>
            <option value="CAR">CAR-CHARTERED ACCOUNTANT REFERENCE</option>
            <option value="CECGA">CECGA-CENTRAL EXCISE &amp; CUSTOMS GOLD CONTROL APPLICATION
            </option>
            <option value="CECGR">CECGR-CE-CUSTOMS GOLD CONTROLL REFERENCE</option>
            <option value="CMP">CMP-PTN. UNDER CHRISTIAN MARRIAGE ACT</option>
            <option value="COMA">COMA-COMPANY APPLICATION</option>
            <option value="COMP">COMP-COMPANY PETITION</option>
            <option value="CS">CS-CIVIL SUITS</option>
            <option value="EA">EA-ELECTION APPLICATION</option>
            <option value="EDA">EDA-ESTATE DUTY APPLICATION</option>
            <option value="EDR">EDR-ESTATE DUTY REFERENCE</option>
            <option value="EP">EP-ELECTION PETITION</option>
            <option value="EXTA">EXTA-EXPENDITURE TAX APPLICATION</option>
            <option value="EXTR">EXTR-EXPENDITURE TAX REFERENCE</option>
            <option value="GTA">GTA-GIFT TAX APPLICATION</option>
            <option value="GTR">GTR-GIFT TAX REFERENCE</option>
            <option value="IAAP">IAAP-PETN. UNDER ARBITRATION ACT</option>
            <option value="ITA">ITA-INCOME TAX APPLICATION</option>
            <option value="ITR">ITR-INCOME TAX REFERENCE</option>
            <option value="OJ109">OJ109-APPEAL UNDER SECTION 109</option>
            <option value="OJA">OJA-O.J.APPEAL</option>
            <option value="OJCAN">OJCAN-CANCELLATION APPLICATION</option>
            <option value="OJCR">OJCR-CRIMINAL CASE</option>
            <option value="OJMP">OJMP-MISC. PETITION</option>
            <option value="OJRP">OJRP-REVIEW PETITION</option>
            <option value="OLR">OLR-OFFICIAL LIQUDATOR REPORT</option>
            <option value="RA">RA-RECTIFICATION APPLICATION</option>
            <option value="RP">RP-REVOCATION PETITION</option>
            <option value="SJC">SJC-SPECIAL JURISDICTION CASES</option>
            <option value="SPTA">SPTA-SUPER PROFIT TAX APPLICATION</option>
            <option value="SPTR">SPTR-SUPER PROFIT TAX REFERENCE</option>
            <option value="SR">SR-STAMP REFERENCE</option>
            <option value="ST(OJ)">ST(OJ)-ST(OJ)</option>
            <option value="STA">STA-SALES TAX APPLICATION</option>
            <option value="STR">STR-SALES TAX REFERENCE</option>
            <option value="SUTA">SUTA-SUR TAX APPLICATION</option>
            <option value="SUTR">SUTR-SUR TAX REFERENCE</option>
            <option value="TAXAP">TAXAP-TAX APPEAL</option>
            <option value="TEP">TEP-TESTAMENTARY PETITION</option>
            <option value="WTA">WTA-WEALTH TAX APPLICATION</option>
            <option value="WTR">WTR-WEALTH TAX REFERENCE</option>
            <option value="X-OBJ(O)">X-OBJ(O)-CROSS OBJECTION </option>
        </optgroup>
   </span>
       `;
    }

    if (value == "Criminal") {
        document.querySelector("#CaseType").innerHTML = `
       <option value="select" disabled>Select</option>
       <span class="criminal">
       <optgroup label="-------CRIMINAL-------">
            <option value="CC">CC-CRIMINAL CONFIRMATION CASE</option>
            <option value="CCASE">CCASE-CRIMINAL CASE</option>
            <option value="CR.A">CR.A-CRIMINAL APPEAL</option>
            <option value="CR.MA">CR.MA-CRIMINAL MISC.APPLICATION</option>
            <option value="CR.RA">CR.RA-CRIMINAL REVISION APPLICATION</option>
            <option value="CRREF">CRREF-CRIMINAL REFERENCE</option>
            <option value="SCR.A">SCR.A-SPECIAL CRIMINAL APPLICATION</option>
        </optgroup>
   </span>
       `;
    }
});