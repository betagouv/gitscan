## Changelog : anssi-recommandations-cyber (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la robustesse de l'application, la correction de vulnérabilités de sécurité et l'optimisation de la gestion des réponses et des sources de documents. Des refactorings importants ont été réalisés pour préparer l'application à de futures évolutions, notamment en simplifiant la gestion des conversations et des retours utilisateurs. L'intégration de Renovate pour la gestion des dépendances a également été finalisée.

### Évolutions fonctionnelles
- Permet de récupérer le document source demandé par l'utilisateur via une nouvelle route GET.
- Amélioration de la gestion des réponses : priorisation des paragraphes "maîtrisés" et filtrage possible de ces derniers.
- Ajout d'un singleton pour charger le fichier de mapping des réponses.
- Implémentation d'une page FAQ (en cours de développement).
- Ajout du tracking Matomo sur le bouton de copie de réponse pour suivre l'utilisation.
- Retour d'une erreur 404 si l'interaction n'est pas trouvée ou si le document source n'est pas accessible.

### Évolutions techniques
- Refactorisation de la gestion des conversations : suppression de l'identifiant de conversation obsolète et utilisation de la conversation pour les retours utilisateurs.
- Mise en place d'un mode de maintenance avec affichage d'une page statique 503.
- Mise à jour de la version de PostgreSQL à 17 pour le développement local.
- Intégration de Renovate pour la gestion automatisée des dépendances.
- Mise en place d'un "cooldown" d'une semaine pour l'installation des dépendances afin d'éviter les instabilités.
- Correction d'un problème de redirection temporaire lors de la création de la conversation.
- Mise à jour de la version de DomPurify en 3.4.2 pour corriger des vulnérabilités.

### Autres changements
- Correction de plusieurs alertes de sécurité Dependabot concernant les dépendances (pytest, dompurify, python-dotenv, cryptography).
- Mise à jour de nombreuses dépendances (eslint, typescript, vite, svelte, etc.) via Renovate.
- Suppression de code obsolète et nettoyage général du code.
- Journalisation de la requête de document source.
- Résolution d'un bug où l'ID de réponse était mal géré.
