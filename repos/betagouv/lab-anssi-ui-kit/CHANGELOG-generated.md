## Changelog : lab-anssi-ui-kit (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à la bibliothèque de composants lab-anssi-ui-kit au cours des 30 derniers jours. Les principales évolutions concernent l'ajout de nouveaux composants, l'amélioration de la gestion des thèmes (notamment avec l'intégration de "Style Dictionary"), et des corrections de bugs pour une meilleure expérience utilisateur. Plusieurs versions mineures ont été publiées pour intégrer ces changements.

### Évolutions fonctionnelles
- Ajout du composant Transcription du DSFR (#0a830e9).
- Amélioration du composant `DsfrButton` avec la gestion des tailles (#adb2476).
- Correction de l'alignement des numéros dans le composant Marellet (#7efdb55).
- Ajout d'un slot pour surcharger le texte du composant `DSFR Highlight` (#0ce5f84).
- Amélioration de l'état "disabled" de la variation "inverted-secondary" du composant `DSFR Button` (#9a99b19).

### Évolutions techniques
- Intégration de "Style Dictionary" pour la gestion des "design tokens" et la transformation en variables CSS (#8c293b7, #0971c05, #fd5f89f, #eb1a98b).
- Amélioration du déploiement des styles de thèmes et du DSFR (#49e0b74).
- Thématisation des variables DSFR selon les couleurs MSS et MSC (#cb0b633, #b70d222).
- Ajout d'une fonction pour définir un attribut `data-` sur les composants thématisables (#892c22b).
- Rendre l'icône 'check' des composants thématisable (#1bae165).
- Amélioration de l'usage des thèmes dans Storybook (#d5a8a28).
- Mise à jour des couleurs du thème MSC (#16127a8).

### Autres changements
- Ajout du thème 'DSFR' au 'switcher' de thèmes de Storybook (#a545bc3).
- Amélioration du contenu du fichier de variables DSFR (#c422334).
- Publication des versions 1.40.0, 1.41.0, 1.41.1, 1.41.2, 1.41.3, 1.41.4 et 1.42.0 (#8728641, #03c0387, #290ab26, #4ebae37, #47e2ffd, #8cd32dd).
