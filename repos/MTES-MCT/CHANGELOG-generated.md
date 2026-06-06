# Synthèse d'activité : MTES-MCT (du 22/05 au 03/06)

## Résumé de l'activité
L'activité récente de l'organisation MTES-MCT a été marquée par des améliorations significatives sur plusieurs fronts.  De nombreuses mises à jour ont été apportées aux applications web existantes, notamment *Dossier Facile* et *Lucca*, avec des améliorations de l'interface utilisateur, de la sécurité et de la gestion des données.  Plusieurs dépôts ont bénéficié d'optimisations de performance et de corrections de bugs. L'accent a également été mis sur l'intégration de nouvelles fonctionnalités, comme l'authentification à deux facteurs pour *Keycloak-FranceConnect* et l'ajout de données de transport routier pour *Ecobalyse*. Enfin, des efforts importants ont été déployés pour améliorer la qualité des données et la documentation, notamment dans les dépôts *acceslibre* et *ecobalyse-schema*.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

*   *Keycloak-FranceConnect* : Activation de l'authentification à deux facteurs (2FA) pour l'identité ProConnect.
*   *Dossier-Facile-Frontend* : Mise à jour des dépendances pour corriger des vulnérabilités (CVE).
*   *Docurba* : Refonte de l'infrastructure de déploiement avec Nginx pour une meilleure sécurité et limitation de débit.

## Autres changements notables
*   *Ecobalyse* : Ajout de données de transport routier pour le Maroc et implémentation du Coefficient de Facteur de Forme (CFF) pour l'emballage alimentaire.
*   *Dahlia* : Création de la première version de l'application web, permettant la gestion des dossiers DALO, DAHO et DAHU.
*   *Lucca* : Ajout de la gestion des adhérents et de la possibilité de cloner un adhérent vers un autre département.
*   *Docurba* : Intégration de Supabase pour l'authentification et création d'une API interne.
*   *Monitorfish* : Ajout de l'affichage des navires sous AIS.
*   *Trackdéchets* : Implémentation de l'authentification à double facteur (2FA).

## Dépôts les plus actifs
*   [Dossier-Facile-Frontend](/repos/MTES-MCT/Dossier-Facile-Frontend) : Améliorations de l'interface utilisateur, correction de bugs et ajout de nouvelles fonctionnalités.
*   [Lucca](/repos/MTES-MCT/Lucca) : Ajout de la gestion des adhérents et amélioration de l'importation des données.
*   [Ecobalyse](/repos/MTES-MCT/Ecobalyse) : Ajout de nouvelles données et amélioration de la modélisation.
*   [Docurba](/repos/MTES-MCT/Docurba) : Refonte de l'infrastructure et ajout de nouvelles fonctionnalités.
*   [Trackdechets](/repos/MTES-MCT/trackdechets) : Implémentation de l'authentification à double facteur et ajout de nouvelles fonctionnalités.
*   [Monitorfish](/repos/MTES-MCT/monitorfish) : Ajout de l'affichage des navires sous AIS.
*   [Dahlia](/repos/MTES-MCT/dahlia) : Création de la première version de l'application.
