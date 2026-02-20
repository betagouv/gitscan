## Changelog : anssi-recommandations-cyber (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à l'interface d'interrogation du modèle d'IA Albert, alimenté par les guides de l'ANSSI. Les modifications incluent une meilleure gestion des conversations, l'ajout de fonctionnalités de reformulation de questions, une gestion améliorée des erreurs et des corrections de bugs pour une expérience utilisateur plus fluide. Des améliorations de sécurité et de maintenance ont également été effectuées.

### Évolutions fonctionnelles
- Ajout de la possibilité de converser avec Albert en conservant l'historique des échanges. (#200b289, #254faef, #c25add6)
- Implémentation d'un reformulateur de question pour améliorer la pertinence des réponses d'Albert. (#368e6ef, #bb0bdc2, #8b32dbb, #3ae7c94, #e5cc552, #dd6bbf1, #c605787, #fa8d59c)
- Possibilité de copier le texte de la réponse au format Markdown. (#591c056, #44f13c7, #390b5de, #c859ad7)
- Ajout des pages CGU et politique de confidentialité. (#c175639)
- Ajout d'un bandeau pour les beta testeurs. (#78c4064)
- Amélioration de l'affichage des messages d'erreur et ajout de la possibilité de réessayer. (#595d513, #61792f3, #c589f4f)

### Évolutions techniques
- Refactorisation de la gestion des routes API pour une meilleure organisation. (#a22b8b7)
- Séparation de la création de conversation et de l'ajout d'interactions. (#0a60f0d, #200b289)
- Implémentation d'une persistance des conversations en base de données. (#61e5d7d, #74e5861, #9deadfb)
- Ajout d'un outil de migration de base de données. (#d38b9bb)
- Utilisation d'une implémentation mémoire pour certains services (Sentry, AdaptateurJournal) pour faciliter les tests et le développement. (#30117c6, #2b4bc6a, #5f8b5e0)
- Mise à jour des dépendances de sécurité (urllib3, eslint). (#5306150, #6961f19, #f745246)
- Suppression de dépendances inutilisées (fastapi-armor). (#c02ea49)
- Amélioration de la gestion des erreurs et de la journalisation. (#595d513, #61792f3, #c589f4f)
- Ajout de tests unitaires et d'intégration. (#200b289)

### Autres changements
- Ajout du type utilisateur `EVALUATION`. (#71c01af)
- Suppression de code mort et de fichiers inutiles. (#34ac072, #94072d3)
- Amélioration de la qualité du code avec Prettier et ESLint. (#67ee405)
- Correction de bugs mineurs et améliorations de l'interface utilisateur. (#449223b, #df35053, #16e5df0, #806c30a, #3da515d, #90e9d8d)
- Uniformisation des noms de variables. (#9bec91b)
- Suppression d'un print oublié. (#277d10e)
