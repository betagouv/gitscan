## Changelog : eva-serveur (30 derniers jours)

### Résumé
Les dernières semaines ont été marquées par d'importantes améliorations pour les utilisateurs d'eva-serveur, notamment l'ajout de fonctionnalités pour la gestion des structures et des utilisateurs, ainsi que des corrections de bugs pour améliorer la stabilité et l'expérience utilisateur. Une attention particulière a été portée à l'intégration d'un nouvel espace "Evapro" avec des fonctionnalités spécifiques et une interface utilisateur améliorée. Des optimisations de performance et des mises à jour de dépendances ont également été réalisées.

### Évolutions fonctionnelles
- Possibilité pour les superadmins de déplacer le dernier admin d'une structure. [#993f22a](https://github.com/betagouv/eva-serveur/commit/993f22a)
- Les utilisateurs peuvent rejoindre une structure existante même si elle n'est pas présente dans l'API officielle. [#893fecd](https://github.com/betagouv/eva-serveur/commit/893fecd)
- Ajout de la possibilité de spécifier un rôle lors de l'envoi d'invitations. [#ab1e9ab](https://github.com/betagouv/eva-serveur/commit/ab1e9ab)
- Les utilisateurs peuvent maintenant paramétrer le code postal. [#15a37b1](https://github.com/betagouv/eva-serveur/commit/15a37b1)
- Ajout d'une modale d'invitation par email avec la possibilité d'envoyer des invitations à des collaborateurs. [#63d5874](https://github.com/betagouv/eva-serveur/commit/63d5874)
- Les comptes supprimés sans évaluations sont maintenant supprimés définitivement. [#09bb9d5](https://github.com/betagouv/eva-serveur/commit/09bb9d5)
- Anonymisation des comptes effacés ayant des évaluations (une fois par mois). [#a11bcf8](https://github.com/betagouv/eva-serveur/commit/a11bcf8)
- Ajout de la possibilité de recréer ou réimporter un questionnaire avec le nom technique d'un questionnaire effacé. [#ed96e4d](https://github.com/betagouv/eva-serveur/commit/ed96e4d)
- Les utilisateurs Evapro peuvent modifier toutes leurs informations. [#581fe5d](https://github.com/betagouv/eva-serveur/commit/581fe5d)
- Ajout de la possibilité de sélectionner un SIRET lors de l'inscription quand il y en a plusieurs. [#9c52c58](https://github.com/betagouv/eva-serveur/commit/9c52c58)
- Les superadmins peuvent affecter le même SIRET à plusieurs structures. [#0cbb72c](https://github.com/betagouv/eva-serveur/commit/0cbb72c)
- Les utilisateurs peuvent télécharger le rapport PDF d'une évaluation Evapro. [#c82b53d](https://github.com/betagouv/eva-serveur/commit/c82b53d)

### Évolutions techniques
- Mise à jour du DSFR de 1.13.0 à 1.14.2. [#2712418](https://github.com/betagouv/eva-serveur/commit/2712418)
- Suppression de l'utilisation de Mailjet pour le tracking. [#9ab6c80](https://github.com/betagouv/eva-serveur/commit/9ab6c80)
- Refactoring du code pour une meilleure lisibilité et maintenabilité.
- Ajout d'un feature flag pour activer/désactiver Evapro via la variable d'environnement `ACTIVE_EVAPRO`. [#c2d0275](https://github.com/betagouv/eva-serveur/commit/c2d0275)
- Suppression de la table `structure_opcos` et modification des relations pour simplifier la gestion des OPCOs.
- Amélioration de la CI et ajout de linters pour garantir la qualité du code.
- Optimisation de la gestion des erreurs et des validations.

### Autres changements
- Mise à jour de la documentation.
- Corrections de typos et amélioration du wording dans l'interface utilisateur.
- Amélioration de l'accessibilité de certains composants.
- Modifications de style pour améliorer l'apparence de l'interface utilisateur.
- Suppression de traces de debug.
- Ajout de tests unitaires et d'intégration.
- Mise à jour de certaines dépendances.
- Suppression de l'adresse email du compte de Démo et renommage des adresses en `anlci.gouv.fr`. [#2fe8ece](https://github.com/betagouv/eva-serveur/commit/2fe8ece)
- Suppression de Matomo et Crisp et ajout de Plausible pour l'analyse. [#56bc36d](https://github.com/betagouv/eva-serveur/commit/56bc36d)
- Correction de l'envoi d'invitations. [#f8316ee](https://github.com/betagouv/eva-serveur/commit/f8316ee)
- Répare la modale de verification de compte. [#d1847fc](https://github.com/betagouv/eva-serveur/commit/d1847fc)
- Ne tente pas d'envoyer un mail de relance aux comptes administratifs. [#8150aaf](https://github.com/betagouv/eva-serveur/commit/8150aaf)
