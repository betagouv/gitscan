## Changelog : proconnect-identite (30 derniers jours, au 16 octobre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur le renforcement de la sécurité des comptes (authentification forte, notifications de sécurité) et l'optimisation des performances du système. Plusieurs améliorations ont été apportées à la gestion des domaines de messagerie et à la stabilité des processus d'authentification pour offrir une expérience plus fluide et sécurisée.

### Évolutions fonctionnelles
- **Sécurité et authentification** :
  - Possibilité de forcer l'authentification à deux facteurs (2FA) par organisation [0ca2613].
  - Vérification du MFA avant de débuter un processus d'enrôlement [#2230](https://github.com/proconnect-gouv/proconnect-identite/issues/2230).
  - Rétablissement de l'interface conditionnelle WebAuthn [4d645bf].
- **Notifications** :
  - Envoi d'un email de confirmation lors de la réinitialisation d'un mot de passe [#2134](https://github.com/proconnect-gouv/proconnect-identite/issues/2134).
  - Envoi d'un email de confirmation lorsqu'un utilisateur quitte une organisation [#2135](https://github.com/proconnect-gouv/proconnect-identite/issues/2135).
- **Corrections et améliorations** :
  - Amélioration de la détection et de la gestion des domaines de messagerie gratuits.
  - Résolution de bugs liés à la validation des emails et à l'affichage des erreurs de correspondance (pays de naissance, informations FranceConnect) [#2162](https://github.com/proconnect-gouv/proconnect-identite/issues/2162), [#2208](https://github.com/proconnect-gouv/proconnect-identite/issues/2208).

### Évolutions techniques
- **Sécurité et performance** :
  - Mise à jour de la politique de limitation de débit (rate limiting) par adresse IP [#2210](https://github.com/proconnect-gouv/proconnect-identite/issues/2210), [#2197](https://github.com/proconnect-gouv/proconnect-identite/issues/2197).
  - Optimisation des appels API en supprimant les appels inutiles vers le RNE lors de l'adhésion à une organisation [7b16383] et en supprimant l'endpoint SIRENE obsolète [#2207](https://github.com/proconnect-gouv/proconnect-identite/issues/2207).
- **Refactoring** :
  - Restructuration et optimisation de la logique des gardes de navigation pour une meilleure maintenance [#2250](https://github.com/proconnect-gouv/proconnect-identite/issues/2250), [#2236](https://github.com/proconnect-gouv/proconnect-identite/issues/2236), [#2241](https://github.com/proconnect-gouv/proconnect-identite/issues/2241).
  - Refonte de la gestion des salutations [#2175](https://github.com/proconnect-gouv/proconnect-identite/issues/2175).
- **Infrastructure et DevOps** :
  - Adoption du versionnage CalVer via `release-it` [8f5388f].
  - Amélioration du suivi des erreurs avec l'ajout de la version de l'application dans les tags Sentry [#2262](https://github.com/proconnect-gouv/proconnect-identite/issues/2262).
  - Mise à jour du schéma de la base de données [0ac21e3].

### Autres changements
- **Données** : Synchronisation de la liste des administrations via Grist [#2264](https://github.com/proconnect-gouv/proconnect-identite/issues/2264).
- **Nettoyage** : Suppression de mots offensants de la liste de mots utilisée pour le diceware [#2266](https://github.com/proconnect-gouv/proconnect-identite/issues/2266) et retrait de code mort dans les fonctions de récupération d'utilisateurs [#2154](https://github.com/proconnect-gouv/proconnect-identite/issues/2154).
