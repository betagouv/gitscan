## Changelog : dialog (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié d'améliorations majeures sur les outils de cartographie, notamment pour le tracé libre et l'utilisation de filtres. L'expérience utilisateur est enrichie par un nouveau tableau de bord, l'export de données en format CSV et une navigation plus fluide. La sécurité et la fiabilité de l'API ont également été renforcées.

### Évolutions fonctionnelles
- **Cartographie et tracé** :
  - Amélioration de l'interface et de la gestion des erreurs lors du tracé libre ([#2033](https://github.com/MTES-MCT/dialog/issues/2033), [#2040](https://github.com/MTES-MCT/dialog/issues/2040)).
  - Ajout de la vérification de présence de rue dans les zones tracées librement ([#2057](https://github.com/MTES-MCT/dialog/issues/2057)).
  - Amélioration des filtres cartographiques (gestion via l'URL [#2052](https://github.com/MTES-MCT/dialog/issues/2052) et correction de l'affichage du filtre "publié" [#2058](https://github.com/MTES-MCT/dialog/issues/2058)).
  - Intégration d'icônes dynamiques pour les limitations de vitesse ([#2077](https://github.com/MTES-MCT/dialog/issues/2077)).
- **Nouvelles fonctionnalités** :
  - Mise en place d'un nouveau tableau de bord ([#2032](https://github.com/MTES-MCT/dialog/issues/2032)).
  - Possibilité d'exporter l'ensemble des réglementations au format CSV ([#2036](https://github.com/MTES-MCT/dialog/issues/2036)).
  - Gestion des inscriptions des mandataires ([#2047](https://github.com/MTES-MCT/dialog/issues/2047)).
- **Interface et navigation** :
  - Ajout du lien "Accueil" dans le fil d'Ariane sur l'ensemble des pages ([#2048](https://github.com/MTES-MCT/dialog/issues/2048)).
  - Affichage du nombre total d'arrêtés dans les pages de listes ([#2059](https://github.com/MTES-MCT/dialog/issues/2059)).
  - Amélioration de la visibilité des organisations dans les formulaires et l'interface ([#2037](https://github.com/MTES-MCT/dialog/issues/2037), [#2023](https://github.com/MTES-MCT/dialog/issues/2023)).
- **Administration et sécurité** :
  - Conservation des logs pour les demandes de réinitialisation de mot de passe ([#2068](https://github.com/MTES-MCT/dialog/issues/2068)).
  - Correction du contenu des adresses de signalement dans l'interface d'administration ([#2038](https://github.com/MTES-MCT/dialog/issues/2038)).

### Évolutions techniques
- **API** :
  - Amélioration globale de l'API ([#2041](https://github.com/MTES-MCT/dialog/issues/2041)).
  - Correction des erreurs de fuseaux horaires ([#2049](https://github.com/MTES-MCT/dialog/issues/2049)) et renforcement de la gestion des exceptions ([#2050](https://github.com/MTES-MCT/dialog/issues/2050)).
- **Données et Analytics** :
  - Intégration d'événements Matomo ([#2061](https://github.com/MTES-MCT/dialog/issues/2061)) et correction de l'envoi de données locales vers l'outil d'analyse ([#2046](https://github.com/MTES-MCT/dialog/issues/2046)).
  - Ajout des mesures SOGELINK dans le transformateur Litteralis ([#2026](https://github.com/MTES-MCT/dialog/issues/2026)).
- **Infrastructure et Build** :
  - Utilisation de Chromium comme shell headless pour les tests ([#2073](https://github.com/MTES-MCT/dialog/issues/2073)).
  - Correction de la génération des URLs publiques via la variable `BASE_URL` ([#2072](https://github.com/MTES-MCT/dialog/issues/2072)).

### Autres changements
- Amélioration de la mise à jour du statut IGN ([#2039](https://github.com/MTES-MCT/dialog/issues/2039)).
