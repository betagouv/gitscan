## Changelog : anssi-recommandations-cyber-data (30 derniers jours)

### Résumé
Ce mois-ci, le projet a connu une refonte significative de l'indexation de documents, avec l'introduction d'un indexeur Albert et des améliorations substantielles de l'indexeur Docling. Ces changements visent à améliorer la robustesse, la performance et la flexibilité du système d'indexation, permettant une meilleure gestion des documents PDF et une intégration plus fluide avec les outils existants. Des corrections de sécurité et des mises à jour de dépendances ont également été effectuées.

### Évolutions fonctionnelles
- Possibilité d'ajouter un seul document à une collection existante. (#14966f0)
- Amélioration de la fusion des blocs de texte en se basant sur leur catégorisation. (e74583c)
- Permet de transformer les tableaux au format Markdown. (cfabc1c)
- Correction de la génération des URLs des guides. (356fda0)

### Évolutions techniques
- Refonte de l'indexation : extraction d'un indexeur Albert dédié. (635f249)
- Refonte de l'indexation : extraction d'une représentation des parties d'une page PDF. (5ecb2d6)
- Refonte de l'indexation : extraction d'une réponse document générique (succès/erreur). (b63de3c)
- Amélioration de l'instanciation de Docling pour une utilisation plus efficace. (7ffb3dc)
- Utilisation de PyPdf pour la lecture des documents PDF. (275ad69)
- Amélioration de la gestion des erreurs lors de l'indexation, permettant de continuer même en cas d'exception. (42f4a38)
- Implémentation de l'indexation avec Docling en utilisant plusieurs processus pour améliorer la performance. (42ca4cc)
- Catégorisation plus fine du contenu des textes pour une meilleure indexation. (2234e04)
- Initialisation d'un indexeur (Albert ou Docling) en fonction de la configuration. (14fc9c2)
- Ajout d'un indexeur Docling. (0beb0cc)
- Correction de la valeur du type utilisateur envoyé à MQC. (e8b3881)
- Ajout du type utilisateur `EVALUATION` lors de l’appel à MQC. (a30eea0)

### Autres changements
- Mise à jour de `deepeval` et `protobuf` suite à une alerte de sécurité. (#22) (45e637e)
- Mise à jour de `wheel` suite à une alerte de sécurité. (#14) (2cb892c)
- Mise à jour de `filelock` pour résoudre une alerte Dependabot. (e4f6de2)
- Corrections diverses pour résoudre les alertes Dependabot. (83e5c9b)
- Suppression de la dépendance obsolète `canvas`. (8b15b9c)
- Modifications des chemins et de la sortie pour les tests "CROSS OS". (e0a17c2)
- Amélioration de la cohérence de l'indexation avec le fichier traité. (4448d06)
- Impression du résultat de l'indexation sur la sortie standard. (3e41af6)
- Retour d'une réponse d'erreur en cas d'échec de l'indexation. (3c89e86)
