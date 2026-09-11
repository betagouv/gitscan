## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 03/09/2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'expérience d'évaluation, la robustesse du processus d'indexation des documents (notamment face aux erreurs d'OCR) et la résolution de plusieurs vulnérabilités de sécurité critiques.

### Évolutions fonctionnelles
- **Évaluation** : Ajout d'une nouvelle interface permettant de lancer et de piloter les évaluations.
- **Backoffice** : 
    - Possibilité de sélectionner une collection spécifique pour modification.
    - Affichage des pages non indexées pour un meilleur suivi.
- **Expérience utilisateur** : Résumé automatique des chemins de sections trop longs pour améliorer la lisibilité.
- **Gestion documentaire** : Ajout d'une fonctionnalité permettant de signaler un document cible comme problématique.

### Évolutions techniques
- **Sécurité** : Correction de plusieurs vulnérabilités critiques et modérées via la mise à jour de dépendances clés (`transformers`, `cryptography`, `idna`, `json-repair`, `pip`, `python-dotenv`, `setuptools`, `soupsieve`) suite aux alertes [#149](https://github.com/betagouv/anssi-recommandations-cyber-data/security/dependabot/149), [#150](https://github.com/betagouv/anssi-recommandations-cyber-data/security/dependabot/150) et autres.
- **Robustesse de l'indexation** : 
    - Amélioration de la résilience de l'OCR face aux erreurs de pages.
    - Permis la poursuite de l'indexation des documents même en cas d'échec partiel de l'OCR sur certaines pages.
- **Optimisation** : Réduction de la fréquence de suivi de l'indexation pour optimiser les ressources système.

### Autres changements
- Mise à jour de la documentation (README).
