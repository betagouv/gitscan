## Changelog : proconnect-identite (30 derniers jours, au 09/10/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur le renforcement de la sécurité (authentification forte, limitation de débit) et l'amélioration de la fiabilité des données (intégration de l'API RNE, validation des emails). Le projet a également progressé sur la protection de la vie privée via l'anonymisation des données exportées et l'optimisation des processus de déploiement.

### Évolutions fonctionnelles
- **Sécurité et authentification** :
    - Possibilité de forcer l'authentification à deux facteurs (2FA) par organisation [#2184](https://github.com/proconnect-gouv/proconnect-identite/pull/2184).
    - Vérification du MFA avant de permettre l'enrôlement d'un nouveau dispositif.
    - Rétablissement de l'interface conditionnelle WebAuthn (Conditional UI) pour une expérience de connexion plus fluide [#2180](https://github.com/proconnect-gouv/proconnect-identite/pull/2180).
- **Gestion des utilisateurs et données** :
    - Amélioration de la validation des adresses email (gestion des domaines gratuits et correction de formats invalides).
    - Normalisation des noms (gestion des accents/diacritiques) pour les processus de certification.
    - Ajout de la "dénomination usuelle" pour les établissements.
    - Anonymisation des intitulés de poste dans les données exportées pour protéger la vie privée.
- **Expérience utilisateur et alertes** :
    - Inclusion du nom de la clé d'accès dans les emails d'alerte de sécurité et lors de la suppression d'une passkey.
    - Correction de l'affichage des erreurs lors de la correspondance de données (birth_country, FranceConnect) [#2162](https://github.com/proconnect-gouv/proconnect-identite/pull/2162).

### Évolutions techniques
- **Sécurité et infrastructure** :
    - Mise à jour et ajustement de la politique de limitation de débit (rate limiting) par adresse IP [#2197](https://github.com/proconnect-gouv/proconnect-identite/pull/2197), [#2166](https://github.com/proconnect-gouv/proconnect-identite/pull/2166).
    - Blocage de l'indexation par les moteurs de recherche via le fichier `robots.txt`.
- **Architecture et optimisation** :
    - Migration vers l'utilisation de l'API RNE pour la récupération des informations d'organisation.
    - Création d'un nouveau dépôt dédié pour la gestion des informations utilisateurs FranceConnect.
    - Refonte de la gestion des salutations (greetings) et du processus de vérification des contacts officiels.
    - Optimisation des performances en réduisant les appels externes (RNE, SIRENE) lors de certaines opérations.
- **CI/CD et déploiement** :
    - Mise en place d'un nouveau workflow de release utilisant le versioning CalVer [#2216](https://github.com/proconnect-gouv/proconnect-identite/pull/2216).

### Autres changements
- Synchronisation régulière de la liste des administrations via Grist.
- Nettoyage du code : suppression de fonctions obsolètes (SIRENE health check) et de code mort.
