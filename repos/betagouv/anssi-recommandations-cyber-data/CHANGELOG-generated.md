## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 03/09/2026)

### Résumé
Cette période a été marquée par l'ajout de fonctionnalités clés pour l'évaluation des modèles et une amélioration significative de la robustesse du processus d'indexation des documents. Un effort majeur a également été consacré à la sécurisation du projet via la correction de plusieurs vulnérabilités critiques dans les dépendances.

### Évolutions fonctionnelles
- **Évaluation** : Mise en place d'une interface dédiée permettant de lancer et de piloter les processus d'évaluation.
- **Gestion du Backoffice** :
    - Possibilité de sélectionner une collection spécifique pour modification.
    - Ajout d'une visibilité sur les pages n'ayant pas pu être indexées.
- **Interface utilisateur** : Amélioration de la lisibilité en résumant les chemins de sections trop longs.

### Évolutions techniques
- **Sécurité** : Correction de nombreuses vulnérabilités critiques et modérées via la mise à jour de dépendances clés (`transformers`, `cryptography`, `idna`, `pip`, `setuptools`, etc.) suite aux alertes Dependabot ([#149](https://github.com/betagouv/anssi-recommandations-cyber-data/security/dependabot/149), [#150](https://github.com/betagouv/anssi-recommandations-cyber-data/security/dependabot/150), [#141](https://github.com/betagouv/anssi-recommandations-cyber-data/security/dependabot/141), [#107](https://github.com/betagouv/anssi-recommandations-cyber-data/security/dependabot/107), etc.).
- **Robustesse de l'indexation** :
    - Amélioration de la résilience de l'OCR face aux erreurs de lecture de pages.
    - L'indexation des documents peut désormais se poursuivre même si certaines pages présentent des erreurs d'OCR.
- **Optimisation** : Réduction de la fréquence de suivi de l'indexation pour optimiser les ressources système.

### Autres changements
- Mise à jour de la documentation (README).
