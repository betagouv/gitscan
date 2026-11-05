## Changelog : histologe (30 derniers jours, au 04 novembre 2026)

### Résumé
Ce mois-ci, le projet a connu une évolution majeure de son interface de gestion (Back Office), notamment avec la refonte complète du module de visites et une meilleure organisation des informations dans les dossiers. L'amélioration des outils de statistiques et l'intégration de nouvelles méthodes d'authentification (OAuth2) renforcent la capacité de suivi et d'interconnexion avec les partenaires territoriaux.

### Évolutions fonctionnelles
- **Gestion des dossiers et visites** : Refonte complète et amélioration du module "Visites" [#6325](https://github.com/MTES-MCT/histologe/issues/6325) et ajout de la fonctionnalité de visite pour les agents [#6553](https://github.com/MTES-MCT/histologe/issues/6553). Les informations du dossier ont été simplifiées par le regroupement des onglets "Foyer" et "Situation" sous un onglet unique "Détails du dossier" [#6423](https://github.com/MTES-MCT/histologe/issues/6423).
- **Améliorations du Back Office** : Ajout de la possibilité de définir des procédures à engager dans les dossiers [#6433](https://github.com/MTES-MCT/histologe/issues/6433) et ajustement des options lors de la clôture des signalements et des affectations [#6436](https://github.com/MTES-MCT/histologe/issues/6436), [#6477](https://github.com/MTES-MCT/histologe/issues/6477). L'affichage des créateurs de suivi a été ajouté pour une meilleure traçabilité [#6492](https://github.com/MTES-MCT/histologe/issues/6492).
- **Expérience utilisateur et interface** : Amélioration de la validation des formulaires côté utilisateur [#6443](https://github.com/MTES-MCT/histologe/issues/6443) et corrections de l'affichage mobile pour le sélecteur de bâtiment [#6527](https://github.com/MTES-MCT/histologe/issues/6527). L'éditeur de texte (TinyMCE) intègre désormais des boutons de lien conformes au design système DSFR [#6425](https://github.com/MTES-MCT/histologe/issues/6425).
- **Données et Interconnexion** : Mise à jour des tableaux de bord statistiques via Metabase [#6435](https://github.com/MTES-MCT/histologe/issues/6435) et mise en place de la connexion OAuth2 pour l'interconnexion avec Nantes Métropole [#6473](https://github.com/MTES-MCT/histologe/issues/6473).
- **Corrections de logique** : Correction de la proposition de réponses lors de la mise en conformité des logements [#6549](https://github.com/MTES-MCT/histologe/issues/6549) et blocage des connexions sur les signalements archivés [#6540](https://github.com/MTES-MCT/histologe/issues/6540).

### Évolutions techniques
- **Infrastructure et Framework** : Mise à jour de Symfony vers la version 8.1.11 [#6640](https://github.com/MTES-MCT/histologe/issues/6640) et optimisation du planning du workflow CI [#6570](https://github.com/MTES-MCT/histologe/issues/6570).
- **Base de données et API** : Mise en cohérence de la structure de la base de données et des entités Doctrine [#6456](https://github.com/MTES-MCT/histologe/issues/6456) et création d'une table pour la gestion des régions [#6494](https://github.com/MTES-MCT/histologe/issues/6494).
- **Outils de développement et Monitoring** : Ajout de la surveillance (watch) pour Metabase [#6616](https://github.com/MTES-MCT/histologe/issues/6616), configuration de l'environnement de debug avec Docker [#6497](https://github.com/MTES-MCT/histologe/issues/6497) et mise à jour de l'éditeur TinyMCE [#6589](https://github.com/MTES-MCT/histologe/issues/6589).
- **IA** : Ajout d'une page de test pour l'API de traitement de documents par IA [#6431](https://github.com/MTES-MCT/histologe/issues/6431).

### Autres changements
- Réorganisation de la structure du dépôt [#5750](https://github.com/MTES-MCT/histologe/issues/5750).
- Nettoyage du code mort [#6531](https://github.com/MTES-MCT/histologe/issues/6531).
