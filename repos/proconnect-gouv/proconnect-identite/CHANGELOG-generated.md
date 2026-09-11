## Changelog : proconnect-identite (30 derniers jours, au 10/09/2026)

### Résumé
Ce mois-ci, le projet a franchi une étape majeure avec la migration de plusieurs composants clés vers une nouvelle architecture de "connecteurs", visant à améliorer la modularité du système. Les utilisateurs bénéficieront d'une meilleure gestion de leur identité FranceConnect et de notifications plus claires, tandis que la fiabilité des données administratives a été renforcée grâce à une intégration plus directe avec Grist.

### Évolutions fonctionnelles
- **Gestion de l'identité FranceConnect** : possibilité de déconnecter une identité FranceConnect ([#2062](https://github.com/proconnect-gouv/proconnect-identite/issues/2062)) et harmonisation du format de la date de dernière mise à jour ([#2121](https://github.com/proconnect-gouv/proconnect-identite/issues/2121)).
- **Sécurité et MFA** : amélioration de la clarté des emails pour la réinitialisation du 2FA ([#2128](https://github.com/proconnect-gouv/proconnect-identite/issues/2128)), déclenchement automatique des Passkeys si déjà configurées ([#2080](https://github.com/proconnect-gouv/proconnect-identite/issues/2080)) et correction de fautes de frappe dans les messages liés au MFA ([#2114](https://github.com/proconnect-gouv/proconnect-identite/issues/2114)).
- **Notifications** : envoi automatique d'un email à l'utilisateur lorsqu'une demande de modération est annulée ([#2079](https://github.com/proconnect-gouv/proconnect-identite/issues/2079)).
- **Interface utilisateur** : corrections de typos et suppression de liens d'aide en double pour une navigation plus fluide.

### Évolutions techniques
- **Migration vers l'architecture "connecteurs"** : refonte majeure impliquant la migration des dépôts de l'authentificateur, de la modération, du client OIDC, ainsi que des gestionnaires d'utilisateurs et d'organisations vers ce nouveau modèle ([#2094](https://github.com/proconnect-gouv/proconnect-identite/issues/2094), [#2095](https://github.com/proconnect-gouv/proconnect-identite/issues/2095), [#2096](https://github.com/proconnect-gouv/proconnect-identite/issues/2096), [#2090](https://github.com/proconnect-gouv/proconnect-identite/issues/2090), [#2089](https://github.com/proconnect-gouv/proconnect-identite/issues/2089), [#2093](https://github.com/proconnect-gouv/proconnect-identite/issues/2093)).
- **Intégration de données (Grist)** : remplacement des appels à l'ADE par des synchronisations directes via Grist pour les listes SIREN et les administrations ([#2078](https://github.com/proconnect-gouv/proconnect-identite/issues/2078), [#3aa8db1](https://github.com/proconnect-gouv/proconnect-identite/issues/3aa8db1)).
- **Sécurité et Robustesse** : correction d'une faille de contournement du code de contact officiel, amélioration de la gestion du rate limiting ([#2138](https://github.com/proconnect-gouv/proconnect-identite/issues/2138)) et restriction du serveur Hono à son chemin de montage ([#2136](https://github.com/proconnect-gouv/proconnect-identite/issues/2136)).
- **CI/CD et Tests** : refonte du workflow de release avec Changesets ([#2146](https://github.com/proconnect-gouv/proconnect-identite/issues/2146)), ajout d'une commande "watch" pour les tests ([#2137](https://github.com/proconnect-gouv/proconnect-identite/issues/2137)) et optimisation du reset de la base de données de test en CI.
- **Refactoring** : simplification des vues de configuration MFA et optimisation des calculs de données.

### Autres changements
- **Nettoyage** : suppression de la variable d'environnement inutilisée `ZAMMAD_TOKEN` ([#2085](https://github.com/proconnect-gouv/proconnect-identite/issues/2085)).
- **Documentation** : mise à jour de la référence de l'Annuaire des Entreprises ([#2075](https://github.com/proconnect-gouv/proconnect-identite/issues/2075)).
