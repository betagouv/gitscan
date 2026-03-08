## Changelog : lab-anssi-ui-kit (30 derniers jours)

### Résumé
Ce changelog présente les évolutions récentes de la bibliothèque de composants lab-anssi-ui-kit. Les principales améliorations concernent l'ajout de nouveaux composants (Table, Range, Transcription), des améliorations sur le composant Table (pagination, gestion d'état vide, contenu riche) et des correctifs liés à la sécurité (nonce et CSP). Des optimisations ont également été apportées pour limiter les déclenchements de la CI et améliorer la documentation.

### Évolutions fonctionnelles
- Ajout du composant `DsfrTable` avec pagination côté client et serveur, gestion de l'état vide, et possibilité d'injecter du contenu riche dans les cellules. [#issue à identifier]
- Ajout du composant `DsfrRange`. [#issue à identifier]
- Ajout du composant `DsfrTranscription`. [#issue à identifier]
- Le composant `DsfrSelect` permet désormais de masquer le label (`hideLabel`) et d'intercepter les changements de valeur (`onvaluechanged`). [#issue à identifier]
- Le composant `DsfrFooter` permet d'afficher uniquement le bloc du bas. [#issue à identifier]
- Possibilité d'injecter du code HTML dans le footer via un nouveau slot. [#301b90a](https://github.com/betagouv/lab-anssi-ui-kit/commit/301b90a)
- Ajout d'un slot pour surcharger le texte du composant `DSFR Highlight`. [#0ce5f84](https://github.com/betagouv/lab-anssi-ui-kit/commit/0ce5f84)
- Ajout du callback `onpagechange` au composant `DsfrPagination` pour intercepter le clic sur les liens. [#issue à identifier]

### Évolutions techniques
- Mise à jour de Vitest vers la version majeure 4+. [#1a97fd4](https://github.com/betagouv/lab-anssi-ui-kit/commit/1a97fd4)
- Mise à jour de ESLint vers la version majeure 10+. [#d1878b7](https://github.com/betagouv/lab-anssi-ui-kit/commit/d1878b7)
- Optimisation de la CI pour limiter les déclenchements aux fichiers impactant le build. [#95eb605](https://github.com/betagouv/lab-anssi-ui-kit/commit/95eb605)
- Correction des expressions régulières pour l'injection du nonce dans les styles, améliorant la sécurité. [#e5089a3](https://github.com/betagouv/lab-anssi-ui-kit/commit/e5089a3)
- Correction d'un problème de CSP. [#55d6358](https://github.com/betagouv/lab-anssi-ui-kit/commit/55d6358)
- Mise à jour des styles du composant `DsfrTable` pour utiliser le CSS minifié. [#ae0f9c1](https://github.com/betagouv/lab-anssi-ui-kit/commit/ae0f9c1)
- Correction de l'offset de la table pour inclure l'unité 'px'. [#41f38dc](https://github.com/betagouv/lab-anssi-ui-kit/commit/41f38dc)

### Autres changements
- Ajout de la documentation concernant la thématisation de la librairie. [#be7987c](https://github.com/betagouv/lab-anssi-ui-kit/commit/be7987c)
- Passage en version 1.44.2, 1.44.1, 1.44.0, 1.43.0, 1.42.0 et 1.41.4. [#79b4d99](https://github.com/betagouv/lab-anssi-ui-kit/commit/79b4d99), [#8ac5f46](https://github.com/betagouv/lab-anssi-ui-kit/commit/8ac5f46), [#71a4031](https://github.com/betagouv/lab-anssi-ui-kit/commit/71a4031), [#a78b2d6](https://github.com/betagouv/lab-anssi-ui-kit/commit/a78b2d6), [#8728641](https://github.com/betagouv/lab-anssi-ui-kit/commit/8728641), [#03c0387](https://github.com/betagouv/lab-anssi-ui-kit/commit/03c0387)
- Mise à jour des dépendances. [#a41b1c1](https://github.com/betagouv/lab-anssi-ui-kit/commit/a41b1c1)
