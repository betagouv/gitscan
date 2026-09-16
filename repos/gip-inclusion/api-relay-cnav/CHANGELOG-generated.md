## Changelog : api-relay-cnav (30 derniers jours, au 15/09/2026)

### Résumé
Cette période a été marquée par l'intégration opérationnelle des appels vers le service InterOps et le renforcement de la traçabilité du système grâce à la mise en place d'un module d'audit complet.

### Évolutions fonctionnelles
- **Intégration InterOps** : Activation des appels vers le service InterOps avec enregistrement automatique des données dans la vue d'identité.
- **Gestion des données** : Amélioration du traitement du champ `sex_code` pour supporter le format entier.

### Évolutions techniques
- **Système d'audit** : Implémentation de nouveaux modèles de données et ajout d'une interface d'administration pour la gestion et le suivi des audits.
- **Conformité API** : Mise à jour des sérialiseurs pour garantir l'alignement avec les contraintes techniques du client InterOps.
- **Refactoring et maintenance** :
    - Ajout d'une fonction utilitaire `get_client` pour simplifier les interactions avec InterOps.
    - Optimisation de la gestion des erreurs et de la structure des tests (déplacement de fonctions vers les factories).
