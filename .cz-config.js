// Customized Commitizen configuration for the problem-solving repository
// This can be used with cz-customizable(https://github.com/leoforfree/cz-customizable)

module.exports = {
    types: [
      { value: 'sol', name: 'sol:     A new problem solution' },
      { value: 'approach', name: 'approach:     A new approach to existing problems' },
      { value: 'lang', name: 'language:     A new language to an existing solution' },
      { value: 'feat', name: 'feat:     A new feature' },
      { value: 'fix', name: 'fix:      A bug fix' },
      { value: 'docs', name: 'docs:     Documentation only changes' },
      {
        value: 'style',
        name:
          'style:    Changes that do not affect the meaning of the code\n            (white-space, formatting, missing semi-colons, etc)',
      },
      {
        value: 'refactor',
        name: 'refactor: A code change that neither fixes a bug nor adds a feature',
      },
      {
        value: 'chore',
        name:
          'chore:    Changes to the build process or auxiliary tools\n            and libraries such as documentation generation',
      },
    ],
  
    
    scopes: [{ name: 'leetcode' }],
    
  
    allowTicketNumber: false,
    isTicketNumberRequired: false,
    ticketNumberPrefix: 'TICKET-',
    ticketNumberRegExp: '\\d{1,5}',

    // it needs to match the value for field type. Eg.: 'fix'
    /*
    scopeOverrides: {
      fix: [
        {name: 'merge'},
        {name: 'style'},
        {name: 'e2eTest'},
        {name: 'unitTest'}
      ]
    },
    */
    // override the messages, defaults are as follows
    messages: {
      type: "Select the type of change that you're committing:",
      scope: '\nDenote the SCOPE of this change (optional):',
      // used if allowCustomScopes is true
      customScope: 'Denote the SCOPE of this change:',
      subject: 'Write a SHORT, IMPERATIVE tense description of the change:\n',
      body: 'Provide a LONGER description of the change (optional). Use "|" to break new line:\n',
      breaking: 'List any BREAKING CHANGES (optional):\n',
      footer: 'List any ISSUES CLOSED by this change (optional). E.g.: #31, #34:\n',
      confirmCommit: 'Are you sure you want to proceed with the commit above?',
    },
  
    allowCustomScopes: true,
    allowBreakingChanges: ['feat', 'fix'],
    // skip any questions you want
    // skipQuestions: ['body'],
  
    // limit subject length
    subjectLimit: 100,
    breaklineChar: '|', // It is supported for fields body and footer.
    // footerPrefix : 'ISSUES CLOSED:'
    // askForBreakingChangeFirst : true, // default is false
  };