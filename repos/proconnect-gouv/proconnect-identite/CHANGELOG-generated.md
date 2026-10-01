## Changelog : proconnect-identite (30 derniers jours, au 30 septembre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur le renforcement de la sécurité et la fiabilisation des données. Les utilisateurs bénéficient d'une meilleure gestion de l'authentification (notamment la possibilité de forcer le double facteur pour certaines organisations) et d'une validation plus rigoureuse des informations saisies (emails, noms). En parallèle, l'infrastructure a été optimisée pour être plus robuste, plus performante et plus respectueuse de la vie privée grâce à une meilleure anonymisation des données exportées.

### Évolutions fonctionnelles
- **Sécurité et Authentification**
  - Possibilité de forcer l'authentification à deux facteurs (2FA) par organisation [#2189](https://github.com/proconnect-gouv/proconnect-identite/pull/2189).
  - Réintroduction de l'interface conditionnelle pour WebAuthn (Passkeys) [#2180](https://github.com/proconnect-gouv/proconnect-identite/pull/2180).
  - Possibilité de déconnecter une identité FranceConnect [#2062](https://github.com/proconnect-gouv/proconnect-identite/pull/2062).
  - Correction d'une faille permettant de contourner le code de contact officiel.
- **Expérience Utilisateur et Validation**
  - Amélioration de la validation des adresses email (gestion des domaines gratuits et correction des formats invalides).
  - Amélioration des notifications de sécurité : inclusion du nom de la clé d'accès supprimée dans les emails d'alerte.
  - Correction de la gestion des diacritiques (accents) lors de la normalisation des noms pour la certification.
  - Nettoyage de l'interface utilisateur (suppression de liens d'aide en doublon).
- **Gestion des données**
  - Utilisation de l'API RNE pour récupérer les informations des organisations.
  - Ajout de la dénomination usuelle des établissements.
  - Anonymisation du champ "métier" (job) dans les données exportées pour renforcer la protection de la vie privée.

### Évolutions techniques
- **Architecture et Refactoring**
  - Migration de la gestion de l'environnement vers l'utilisation de "feature flags".
  - Découplage de certaines dépendances (TrancheEffectifs, types WebAuthn) pour une gestion locale et autonome.
  - Création d'un nouveau dépôt dédié à la gestion des informations utilisateur FranceConnect.
  - Homogénéisation de l'utilisation des méthodes `get` et `find` au sein des services de données (repositories).
- **Sécurité et Performance**
  - Augmentation des limites de débit (rate limiting) basées sur l'IP pour l'API [#2197](https://github.com/proconnect-gouv/proconnect-identite/pull/2197) et optimisation de leur gestion [#2166](https://github.com/proconnect-gouv/proconnect-identite/pull/2166).
  - Blocage de l'indexation par les moteurs de recherche via la configuration du fichier `robots.txt`.
  - Restriction du serveur Hono à son chemin de montage pour limiter la surface d'exposition.
- **Maintenance et Tests**
  - Suppression des points de terminaison (endpoints) SIRENE obsolètes et nettoyage des tests de santé (health checks) associés.
  - Amélioration de la robustesse des tests d'intégration via le mock de l'API de "debounce".

### Autres changements
- Synchronisation régulière de la liste des administrations via Grist.
- Corrections de typographies dans la documentation et les messages de l'interface.
