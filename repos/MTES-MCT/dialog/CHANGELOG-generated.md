## Changelog : dialog (30 derniers jours, au 12 août 2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié d'une refonte visuelle de son interface (header et footer) et d'améliorations significatives de l'expérience utilisateur, notamment sur la cartographie et la validation des formulaires. De nouvelles fonctionnalités de communication par email et des capacités de recherche enrichies via l'API ont également été déployées pour faciliter l'accès à l'information réglementaire.

### Évolutions fonctionnelles
- **Interface et Expérience Utilisateur (UX) :**
    - Refonte du header [#2016](https://github.com/MTES-MCT/dialog/issues/2016) et extension du footer [#2015](https://github.com/MTES-MCT/dialog/issues/2015).
    - Amélioration de la cartographie : ajout de points de PR [#2005](https://github.com/MTES-MCT/dialog/issues/2005), retravail des légendes [#1984](https://github.com/MTES-MCT/dialog/issues/1984) et correction de l'icône du filtre poids lourd [#2020](https://github.com/MTES-MCT/dialog/issues/2020).
    - Sécurisation de la saisie : ajout d'une alerte en cas de modifications non sauvegardées sur les formulaires d'arrêté [#2007](https://github.com/MTES-MCT/dialog/issues/2007) et validation immédiate du numéro de rue côté client [#1999](https://github.com/MTES-MCT/dialog/issues/1999).
    - Corrections d'affichage : ajustement du padding pour les exceptions de villes entières [#2021](https://github.com/MTES-MCT/dialog/issues/2021) et correction du filtre de type de véhicules [#1992](https://github.com/MTES-MCT/dialog/issues/1992).
- **Nouvelles fonctionnalités :**
    - Amélioration du système d'email : ajout de la fonction "répondre à" via l'utilisateur actuel [#2019](https://github.com/MTES-MCT/dialog/issues/2019) et envoi d'emails de suivi après abonnement [#2003](https://github.com/MTES-MCT/dialog/issues/2003).
    - Gestion des restrictions : possibilité d'appliquer une restriction sur une zone [#1998](https://github.com/MTES-MCT/dialog/issues/1998) et migration des polygones en zones de restriction [#2006](https://github.com/MTES-MCT/dialog/issues/2006).
    - Back-office : ajout d'un bouton pour l'envoi de rapports IGN [#1995](https://github.com/MTES-MCT/dialog/issues/1995).
- **Corrections :**
    - Résolution du problème de pièces jointes manquantes sur les arrêtés [#1990](https://github.com/MTES-MCT/dialog/issues/1990).
    - Amélioration de la gestion des exceptions sur les restrictions de villes entières [#1949](https://github.com/MTES-MCT/dialog/issues/1949).

### Évolutions techniques
- **API :**
    - Ajout de la recherche de réglementation par code ville d'organisation [#2008](https://github.com/MTES-MCT/dialog/issues/2008).
    - Nouvel endpoint pour récupérer les arrêtés par organisation [#1967](https://github.com/MTES-MCT/dialog/issues/1967).
    - Passage des données JSON de la réglementation de l'accès privé à l'accès public [#1997](https://github.com/MTES-MCT/dialog/issues/1997).
- **Données et Infrastructure :**
    - Correction de la synchronisation vers Grist [#2002](https://github.com/MTES-MCT/dialog/issues/2002).
    - Mise en place du suivi d'événements Matomo pour le téléchargement des arrêtés [#2004](https://github.com/MTES-MCT/dialog/issues/2004).
    - Corrections de bugs de base de données et de requêtes (stockage vide [#1979](https://github.com/MTES-MCT/dialog/issues/1979) et clause `andwhere` [#1985](https://github.com/MTES-MCT/dialog/issues/1985)).

### Autres changements
- Suppression de la notification d'avertissement pour les organisations incomplètes [#2018](https://github.com/MTES-MCT/dialog/issues/2018).
- Modification du processus d'envoi des rapports IGN (suppression de l'automatisme) [#1991](https://github.com/MTES-MCT/dialog/issues/1991).
