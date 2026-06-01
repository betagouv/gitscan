## Changelog : proconnect-identite (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des informations relatives aux services publics, la migration progressive vers une nouvelle méthode d'envoi d'emails, et des corrections pour améliorer la stabilité et la fiabilité de la plateforme. Des mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la performance.

### Évolutions fonctionnelles
- Ajout d'une description d'erreur OIDC pour faciliter le diagnostic des problèmes d'authentification avec PCF. [#1926](https://github.com/proconnect-gouv/proconnect-identite/pull/1926)
- Modification du motif de rejet des demandes de certification : remplacement du motif par un message invitant l'utilisateur à consulter son email pour plus d'informations. [#1927](https://github.com/proconnect-gouv/proconnect-identite/pull/1927)
- Début de la migration de l'envoi d'emails depuis MonComptePro vers une nouvelle solution, avec ajout du nom de l'expéditeur. [#1930](https://github.com/proconnect-gouv/proconnect-identite/pull/1930)
- Création d'un client dédié pour l'environnement de pré-production de la fédération, incluant la mise à jour des identifiants et secrets correspondants. [#1937](https://github.com/proconnect-gouv/proconnect-identite/pull/1937)

### Évolutions techniques
- Implémentation d'une nouvelle fonction `computeIsServicePublic` pour déterminer si un organisme est un service public, utilisant un nouvel algorithme. [#1945](https://github.com/proconnect-gouv/proconnect-identite/pull/1945)
- Refactoring du seed des tests E2E pour utiliser un hook `before` afin d'améliorer la performance et la fiabilité. [#1925](https://github.com/proconnect-gouv/proconnect-identite/pull/1925)
- Correction de l'importation du type `pg` pour une meilleure compatibilité avec les bundlers de navigateurs. [#1947](https://github.com/proconnect-gouv/proconnect-identite/pull/1947)
- Amélioration de la granularité du ratio d'envoi d'emails alternatifs. [#1951](https://github.com/proconnect-gouv/proconnect-identite/pull/1951)
- Ajout de la compatibilité ascendante pour l'algorithme `is-service-public`. [#1956](https://github.com/proconnect-gouv/proconnect-identite/pull/1956)
- Modification de la table `moderations` pour inclure les champs `end_user_reason` et `allow_editing`. [#1954](https://github.com/proconnect-gouv/proconnect-identite/pull/1954)
- Renommage de `is-service-public` en `compute-service-public-info`. [#1952](https://github.com/proconnect-gouv/proconnect-identite/pull/1952)

### Autres changements
- Ajout d'un script pour mettre à jour la liste des administrations depuis un fichier Grist. [#1935](https://github.com/proconnect-gouv/proconnect-identite/pull/1935) et [#1946](https://github.com/proconnect-gouv/proconnect-identite/pull/1946)
- Ajout d'un workflow pour exécuter le script de mise à jour de l'annuaire des entreprises localement. [#1943](https://github.com/proconnect-gouv/proconnect-identite/pull/1943)
- Ajout d'un workflow dispatch pour lancer manuellement des tâches. [#1945](https://github.com/proconnect-gouv/proconnect-identite/pull/1945)
- Mise à jour de la documentation et de la configuration pour refléter les changements.
- Correction d'un problème empêchant l'exécution du script de mise à jour de l'annuaire des entreprises. [#1943](https://github.com/proconnect-gouv/proconnect-identite/pull/1943)
