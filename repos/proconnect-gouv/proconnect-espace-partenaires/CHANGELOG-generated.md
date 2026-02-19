## Changelog : proconnect-espace-partenaires (30 derniers jours)

### Résumé
Cette mise à jour apporte des corrections mineures à l'interface utilisateur, notamment au niveau des messages d'avertissement et des clés utilisées. La documentation a également été mise à jour pour inclure des informations sur la compatibilité avec l'authentification à deux facteurs (2FA). Des mises à jour de dépendances ont été effectuées pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- Correction d'un message d'avertissement (#229).
- Mise à jour de la documentation pour inclure un avertissement concernant la compatibilité avec l'authentification à deux facteurs (2FA) (#227).
- Correction d'une clé incorrecte (#228).

### Évolutions techniques
- Refactorisation de la commande `npm install` pour plus de sécurité (#228).
- Suppression de code redondant et de paramètres inutilisés (#228).
- Mise à jour de la dépendance `proconnect-gouv/federation/api-partner` vers les versions `750172a` (#239), `eb7891b` (#235) et `3c20054` (#233).
- Mise à jour de la dépendance `@playwright/test` vers la version 1.58.1 dans le dossier `/e2e` (#240).
- Mise à jour des dépendances `@uuv/playwright` vers la version 3.58.0 dans le dossier `/e2e` (#236).
- Mise à jour des dépendances `preact` vers la version 10.28.2 (#211).
- Mise à jour des dépendances `lodash` (#231, #230).
- Réorganisation du code (#241).

### Autres changements
- Nettoyage du code et suppression de code inutile (#228).
