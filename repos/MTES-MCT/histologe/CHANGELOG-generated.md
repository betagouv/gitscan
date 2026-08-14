## Changelog : histologe (30 derniers jours, au 13 août 2026)

### Résumé
Ce mois a été marqué par un renforcement significatif de la "Démarche Accélérée", notamment via l'automatisation de la clôture des dossiers inactifs et une meilleure communication avec les bailleurs. Le Back-office a été enrichi de nouveaux outils de gestion (import d'arrêtés, mention de partenaires, historique des adresses) et de meilleures visibilités sur les erreurs de synchronisation. Enfin, des efforts importants ont été portés sur la sécurité et l'accessibilité du parcours utilisateur.

### Évolutions fonctionnelles
- **Démarche Accélérée**
  - Automatisation de la clôture des dossiers inactifs [#6178](https://github.com/MTES-MCT/histologe/issues/6178).
  - Amélioration du processus de clôture pour les bailleurs et la gestion des blocages locataires [#6153](https://github.com/MTES-MCT/histologe/issues/6153), [#6162](https://github.com/MTES-MCT/histologe/issues/6162).
  - Partage des informations de clôture d'injonction avec les bailleurs [#6185](https://github.com/MTES-MCT/histologe/issues/6185).
- **Gestion Back-office (BO)**
  - Possibilité de mentionner un partenaire dans un signalement [#6176](https://github.com/MTES-MCT/histologe/issues/6176).
  - Nouveaux droits de clôture de dossiers pour les RT [#6186](https://github.com/MTES-MCT/histologe/issues/6186) et pour les partenaires [#6124](https://github.com/MTES-MCT/histologe/issues/6124).
  - Importation de l'historique des arrêtés [#6133](https://github.com/MTES-MCT/histologe/issues/6133) avec amélioration des messages d'erreur [#6189](https://github.com/MTES-MCT/histologe/issues/6189).
  - Meilleure visibilité pour les administrateurs sur les erreurs de synchronisation d'affectations [#6144](https://github.com/MTES-MCT/histologe/issues/6144).
  - Mise en place d'un socle front pour l'historique des adresses [#6063](https://github.com/MTES-MCT/histologe/issues/6063).
  - Ajout d'un bandeau de communication dans l'interface [#6191](https://github.com/MTES-MCT/histologe/issues/6191).
- **Expérience Utilisateur & Accessibilité**
  - Amélioration de l'accessibilité clavier pour la sélection de bâtiment [#6038](https://github.com/MTES-MCT/histologe/issues/6038).
  - Optimisation de l'interface des notes personnelles et ajout de tags dans le parcours "SA" [#6184](https://github.com/MTES-MCT/histologe/issues/6184), [#6132](https://github.com/MTES-MCT/histologe/issues/6132).
- **Corrections de bugs**
  - Correction du filtrage des listes de signalements sans agent [#6214](https://github.com/MTES-MCT/histologe/issues/6214).
  - Résolution d'erreurs de contraintes d'intégrité (doublons) [#6205](https://github.com/MTES-MCT/histologe/issues/6205) et de scores API nuls [#6171](https://github.com/MTES-MCT/histologe/issues/6171).
  - Divers correctifs sur les relances bailleurs, les contrôles de dates et l'affichage des boutons [#6142](https://github.com/MTES-MCT/histologe/issues/6142), [#6084](https://github.com/MTES-MCT/histologe/issues/6084), [#6130](https://github.com/MTES-MCT/histologe/issues/6130).

### Évolutions techniques
- **Sécurité & API**
  - Ajout de la traçabilité (Correlation-ID) et diagnostic d'IP sortante pour les erreurs 401 sur l'API RIAL [#6228](https://github.com/MTES-MCT/histologe/issues/6228).
  - Analyse post-mortem suite à une vulnérabilité signalée via YesWeHack [#6223](https://github.com/MTES-MCT/histologe/issues/6223).
  - Amélioration du feedback sur les brouillons de signalement [#6207](https://github.com/MTES-MCT/histologe/issues/6207).
- **Architecture & Performance**
  - Migration du socle pour la gestion des adresses des signalements [#6202](https://github.com/MTES-MCT/histologe/issues/6202).
  - Optimisation des performances sur les filtres de dossiers sans activité [#6125](https://github.com/MTES-MCT/histologe/issues/6125) et les requêtes `job_event` [#6158](https://github.com/MTES-MCT/histologe/issues/6158).
  - Montée de version du framework Symfony [#6168](https://github.com/MTES-MCT/histologe/issues/6168) et nettoyage des dépréciations de code [#6160](https://github.com/MTES-MCT/histologe/issues/6160).
- **Infrastructure & CI/CD**
  - Mise à jour de l'image Ubuntu dans la CI pour l'évolution de la stack Scalingo [#6151](https://github.com/MTES-MCT/histologe/issues/6151).
