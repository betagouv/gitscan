## Changelog : anssi-recommandations-cyber (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout d'un système de feedback utilisateur pour améliorer la qualité des réponses fournies par l'IA.  Des corrections et des optimisations ont également été apportées pour améliorer l'expérience utilisateur et la maintenabilité du code.

### Évolutions fonctionnelles
- Ajout d'un formulaire permettant aux utilisateurs de donner leur avis sur les réponses obtenues. [#1](https://github.com/betagouv/anssi-recommandations-cyber/pulls/1 - *lien fictif pour l'exemple*)
- Possibilité de compléter les avis utilisateurs avec des informations supplémentaires.
- Affichage des retours utilisateurs dans l'interface.
- Route API `/api/avis` exposée pour la soumission des avis utilisateurs.
- Les avis soumis sont maintenant consignés.
- Amélioration de l'affichage du contenu des paragraphes.
- Correction d'un bug empêchant l'affichage de la question après sélection d'une suggestion.
- Déroulement par défaut des sources dans l'interface.
- Amélioration de l'expérience utilisateur en scrollant vers le dernier message de l'utilisateur.

### Évolutions techniques
- Refactorisation du nommage des identifiants de collections et d'interactions pour plus de cohérence.
- Mise à jour de la version de Starlette pour corriger une vulnérabilité de sécurité.
- Épingle des versions des dépendances des GitHub Actions pour assurer la reproductibilité des builds.
- Utilisation d'une variable d'environnement pour la configuration.

### Autres changements
- Nettoyage de la configuration de la CI.
- Suppression d'un log inutile.
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité : `dompurify`, `svelte`, `vite`, `cryptography`. (Ces mises à jour sont gérées par Renovate)
