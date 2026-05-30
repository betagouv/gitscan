# Synthèse d'activité : MTES-MCT (du 13/05 au 29/05)

## Résumé de l'activité
L'activité récente de l'organisation MTES-MCT a été marquée par une forte concentration sur l'amélioration des plateformes existantes et l'ajout de nouvelles fonctionnalités pour répondre aux besoins des utilisateurs. Plusieurs dépôts ont bénéficié de corrections de bugs, d'optimisations de performance et d'améliorations de l'interface utilisateur. Des efforts importants ont également été déployés pour renforcer la sécurité des applications, notamment avec l'implémentation de l'authentification à deux facteurs et la correction de vulnérabilités. On note des avancées significatives sur les projets *dialog*, *dossierfacile*, *ecobalyse* et *monitorfish* avec des améliorations notables pour les agents et les utilisateurs finaux. Plusieurs dépôts ont également mis l'accent sur l'amélioration de la qualité du code et la maintenance technique.

## Sécurité
Plusieurs dépôts ont intégré des améliorations de sécurité :
- Correction de vulnérabilités dans [ecobalyse-data](/repos/MTES-MCT/ecobalyse-data) et [dossierfacile-frontend](/repos/MTES-MCT/Dossier-Facile-Frontend) via la mise à jour de dépendances.
- Implémentation de l'authentification à deux facteurs (2FA) dans [mobilic-api](/repos/MTES-MCT/mobilic-api) et [Keycloak-FranceConnect](/repos/MTES-MCT/Keycloak-FranceConnect).
- Correction d'une vulnérabilité IDOR dans [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend).
- Correction d'une vulnérabilité sur l'endpoint d'autocomplete dans [mesads](/repos/MTES-MCT/mesads).

## Autres changements notables
- Refonte de l'interface utilisateur de la page de revente dans [boris](/repos/MTES-MCT/boris).
- Refactorisation importante du code dans [resorption-bidonvilles](/repos/MTES-MCT/resorption-bidonvilles) et [dialog](/repos/MTES-MCT/dialog).
- Intégration de nouvelles sources de données dans [dialog-integrations](/repos/MTES-MCT/dialog-integrations).
- Mise en place d'une authentification par token dans [ecobalyse-runner](/repos/MTES-MCT/ecobalyse-runner).
- Refonte du schéma de données dans [acceslibre-schema](/repos/MTES-MCT/acceslibre-schema).
- Migration vers un format datapackage pour une meilleure gestion des schémas dans [acceslibre-schema](/repos/MTES-MCT/acceslibre-schema).

## Dépôts les plus actifs
- [zero-logement-vacant](/repos/MTES-MCT/zero-logement-vacant) : Améliorations de l'UX, gestion des campagnes et refactorisation du code.
- [vizeau](/repos/MTES-MCT/vizeau) : Ajout de nouvelles vues synthétiques et améliorations de la visualisation des données.
- [trackdechets](/repos/MTES-MCT/trackdechets) : Ajout de fonctionnalités BSFF et implémentation de l'authentification à deux facteurs.
- [dialog](/repos/MTES-MCT/dialog) : Amélioration de la cartographie, de la gestion des arrêtés et de l'expérience utilisateur.
- [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) : Amélioration de l'interface d'administration et correction de bugs.
- [ecobalyse](/repos/MTES-MCT/ecobalyse) : Ajout de nouvelles informations sur les produits alimentaires et amélioration de la gestion des données.
- [monitorfish](/repos/MTES-MCT/monitorfish) : Intégration de l'affichage des navires AIS et amélioration de la gestion des préavis.
