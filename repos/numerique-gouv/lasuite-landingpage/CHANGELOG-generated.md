## Changelog : lasuite-landingpage (30 derniers jours, au 23 octobre 2026)

### Résumé
Ce mois-ci, la plateforme a été enrichie de nouveaux outils d'interaction, notamment une modale de contact, et a bénéficié de plusieurs mises à jour de contenus pour informer les utilisateurs sur les actualités (Tchap, Resana). Des améliorations techniques ont également été apportées pour intégrer plus efficacement le site de l'événement "On fait suite".

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** : Ajout d'une modale de contact pour faciliter les échanges ([#271](https://github.com/numerique-gouv/lasuite-landingpage/issues/271)).
- **Mises à jour de contenu** :
    - Actualisation de la section "Hero" avec un nouveau teaser ([#272](https://github.com/numerique-gouv/lasuite-landingpage/issues/272)).
    - Mise à jour des informations concernant Tchap ([#265](https://github.com/numerique-gouv/lasuite-landingpage/issues/265)) et ajout d'un webinaire/calendrier pour Resana 2027 ([#268](https://github.com/numerique-gouv/lasuite-landingpage/issues/268)).
    - Actualisation du compteur d'utilisateurs et de l'icône du header pour "On fait suite" ([#260](https://github.com/numerique-gouv/lasuite-landingpage/issues/260)).
- **Corrections** : Résolution d'un problème d'affichage du widget d'intégration sur les applications hôtes ([#277](https://github.com/numerique-gouv/lasuite-landingpage/issues/277)).
- **Communication** : Publication d'annonces concernant les périodes de maintenance du site ([#261](https://github.com/numerique-gouv/lasuite-landingpage/issues/261), [#259](https://github.com/numerique-gouv/lasuite-landingpage/issues/259)).

### Évolutions techniques
- **Routage et infrastructure** : 
    - Mise en place du service du site de l'événement "On fait suite" sous le chemin `/onfaitsuite` ([#264](https://github.com/numerique-gouv/lasuite-landingpage/issues/264)).
    - Optimisation de la configuration des réécritures (rewrites) pour assurer la coexistence du nouveau chemin et des APIs ([#273](https://github.com/numerique-gouv/lasuite-landingpage/issues/273)).
