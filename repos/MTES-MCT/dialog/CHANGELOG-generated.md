## Changelog : dialog (30 derniers jours, au 19/08/2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié d'une amélioration significative de l'expérience utilisateur, notamment grâce à une refonte visuelle de l'interface (header et footer) et une meilleure gestion des formulaires (alertes de perte de données, validation en temps réel). Les outils cartographiques ont été enrichis et les communications par email ont été optimisées pour faciliter les échanges.

### Évolutions fonctionnelles
- **Cartographie et SIG** : 
    - Ajout de l'affichage des points de passage (PR) sur la carte [#2005](https://github.com/MTES-MCT/dialog/issues/2005).
    - Amélioration de la clarté avec une refonte des légendes cartographiques [#1984](https://github.com/MTES-MCT/dialog/issues/1984) et correction des icônes de filtres pour les poids lourds [#2020](https://github.com/MTES-MCT/dialog/issues/2020), [#1975](https://github.com/MTES-MCT/dialog/issues/1975).
    - Possibilité d'appliquer une restriction sur une zone spécifique [#1998](https://github.com/MTES-MCT/dialog/issues/1998).
- **Interface et Expérience Utilisateur (UX)** :
    - Refonte visuelle du header [#2016](https://github.com/MTES-MCT/dialog/issues/2016) et extension du footer [#2015](https://github.com/MTES-MCT/dialog/issues/2015).
    - Sécurisation de la saisie : ajout d'une alerte en cas de modifications non sauvegardées sur les formulaires d'arrêté [#2007](https://github.com/MTES-MCT/dialog/issues/2007) et validation immédiate du numéro de rue lors de la saisie [#1999](https://github.com/MTES-MCT/dialog/issues/1999).
    - Amélioration de la navigation : possibilité de zoomer sur une organisation depuis un formulaire en lecture seule [#2023](https://github.com/MTES-MCT/dialog/issues/2023).
- **Communication** :
    - Mise en place d'emails de suivi après une inscription [#2003](https://github.com/MTES-MCT/dialog/issues/2003).
    - Amélioration des emails avec l'ajout de l'adresse de réponse ("reply-to") correspondant à l'utilisateur actuel [#1936](https://github.com/MTES-MCT/dialog/issues/1936), [#2019](https://github.com/MTES-MCT/dialog/issues/2019).

### Évolutions techniques
- **API** : 
    - Ajout de la recherche de réglementation par code commune de l'organisation [#2008](https://github.com/MTES-MCT/dialog/issues/2008).
    - Passage des données JSON des réglementations de l'accès privé à l'accès public [#1997](https://github.com/MTES-MCT/dialog/issues/1997).
    - Correction de la récupération des identifiants d'interdiction de circulation via le nom [#1968](https://github.com/MTES-MCT/dialog/issues/1968).
- **Données et SIG** :
    - Migration des polygones vers le format "zones de restriction" [#2006](https://github.com/MTES-MCT/dialog/issues/2006).
    - Intégration des mesures SOGELINK dans le processus de transformation des données [#2026](https://github.com/MTES-MCT/dialog/issues/2026).
- **Administration** :
    - Ajout d'un bouton dans le back-office pour l'envoi de rapports IGN [#1995](https://github.com/MTES-MCT/dialog/issues/1995).
    - Optimisation de l'affichage des utilisateurs administrateurs [#1972](https://github.com/MTES-MCT/dialog/issues/1972).

### Autres changements
- **Corrections de bugs** : Résolution de problèmes concernant les pièces jointes [#1990](https://github.com/MTES-MCT/dialog/issues/1990), la synchronisation vers Grist [#2002](https://github.com/MTES-MCT/dialog/issues/2002), le stockage des réglementations vides [#1979](https://github.com/MTES-MCT/dialog/issues/1979) et les mises à jour de données topographiques [#2030](https://github.com/MTES-MCT/dialog/issues/2030).
- **Maintenance et Nettoyage** : 
    - Suppression de l'envoi automatique des rapports IGN [#1991](https://github.com/MTES-MCT/dialog/issues/1991).
    - Suppression des notifications d'avertissement pour les organisations incomplètes [#2018](https://github.com/MTES-MCT/dialog/issues/2018).
    - Ajout du suivi d'événements Matomo pour les téléchargements de réglementation [#2004](https://github.com/MTES-MCT/dialog/issues/2004).
