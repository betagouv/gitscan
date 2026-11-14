## Changelog : proconnect-identite (30 derniers jours, au 15 novembre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec l'introduction des mots de récupération pour sécuriser l'accès aux comptes en cas de perte de l'authentification forte. Parallèlement, une refonte majeure de la surveillance (logging et monitoring) a été déployée pour améliorer la détection d'incidents, accompagnée de nombreuses optimisations de l'expérience utilisateur via une meilleure gestion des redirections et des erreurs.

### Évolutions fonctionnelles
- **Sécurité et récupération de compte**
  - Introduction de la possibilité de se connecter via des mots de récupération ([#2285](https://github.com/proconnect-gouv/proconnect-identite/issues/2285)).
  - Sécurisation du processus : l'authentification multi-facteurs (MFA) est désormais requise avant de pouvoir générer ces mots ([#2471](https://github.com/proconnect-gouv/proconnect-identite/issues/2471)).
  - Amélioration de l'accompagnement : suggestion de génération des mots de récupération après la configuration du MFA ou lors de chaque connexion.
  - Notifications par email lors de la création ou de la régénération des mots de récupération ([#2409](https://github.com/proconnect-gouv/proconnect-identite/issues/2409)).
- **Expérience utilisateur et navigation**
  - Amélioration de la gestion des erreurs : remplacement de plusieurs pages d'erreur par des redirections plus fluides (cas de FranceConnect, réinitialisation de mot de passe, ou vérification de contact officiel).
  - Gestion des organisations : suppression automatique des membres d'un domaine lorsqu'il est refusé ([#2453](https://github.com/proconnect-gouv/proconnect-identite/issues/2453)).
  - Correction de comportements erronés lors de l'abandon de certifications ou de la sélection d'organisations.

### Évolutions techniques
- **Observabilité et Monitoring**
  - Refonte complète du système de logs : passage au format JSON et adoption du standard OpenTelemetry pour une meilleure traçabilité.
  - Renforcement du monitoring avec l'ajout de compteurs pour les événements de sécurité (échecs de passkeys, attaques CSRF, limites de débit/rate-limiting, rejeux de tokens).
  - Optimisation de Sentry : meilleure distinction des environnements, masquage des données sensibles (codes OAuth) et conservation systématique des traces pour les erreurs et redirections.
- **Architecture et Refactoring**
  - Migration de la gestion des suggestions d'organisations vers Drizzle ORM ([#2396](https://github.com/proconnect-gouv/proconnect-identite/issues/2396)).
  - Consolidation des contrôleurs de configuration TOTP ([#2447](https://github.com/proconnect-gouv/proconnect-identite/issues/2447)).
  - Amélioration de la gestion des sessions en liant l'organisation sélectionnée à la session et au client ([#2289](https://github.com/proconnect-gouv/proconnect-identite/issues/2289)).
  - Validation des données de session Express via Zod ([#2242](https://github.com/proconnect-gouv/proconnect-identite/issues/2242)).
- **Infrastructure et CI/CD**
  - Auto-hébergement du conteneur Matomo Tag Manager ([#2267](https://github.com/proconnect-gouv/proconnect-identite/issues/2267)).
  - Optimisation des builds Docker via la mise en cache des dépendances npm.
  - Renforcement de la sécurité des workflows GitHub Actions (limitation des permissions des tokens).

### Autres changements
- **Nettoyage**
  - Mise à jour de la liste de mots Diceware pour supprimer les termes offensants ou sensibles.
