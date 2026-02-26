## Changelog : anssi-recommandations-cyber-data (30 derniers jours)

### Résumé
Ce projet a connu des améliorations récentes axées sur la flexibilité de l'indexation de documents et la correction de problèmes liés à l'intégration avec les services MQC. Des mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité du système.

### Évolutions fonctionnelles
- Possibilité de transmettre un fichier JSON pour l'indexation.
- Ajout des options pour le document `anssi-fondamentaux-securisation-poste-multi-environnements-v1-0.pdf`.
- Permet d'ajouter un seul document à une collection existante.
- Correction de la génération des URLs des guides.
- Correction de la valeur du type utilisateur envoyé à MQC, ajout du type `EVALUATION` lors de l’appel à MQC.

### Évolutions techniques
- Refactorisation du code pour extraire la fonction `cree_document_pdf` et rapatrier `collecte_document_pdf` dans son script.
- Ajout d'un adaptateur `ClientAlbert` pour faciliter l'intégration avec Albert.
- Mise à jour des dépendances `deepeval` et `protobuf` suite à une alerte de sécurité (Dependabot #22).
- Suppression de la dépendance obsolète `canvas`.

### Autres changements
- Modifications des chemins et de la sortie pour permettre l'exécution des tests sur différents systèmes d'exploitation ("CROSS OS").
- Modification de la collection d'un PDF pour spécifier le fichier.
