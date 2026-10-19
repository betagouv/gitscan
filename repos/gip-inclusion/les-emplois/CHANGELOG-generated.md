## Changelog : les-emplois (30 derniers jours, au 16/10/2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante avec la refonte complète du parcours d'orientation pour s'aligner sur les standards de data·inclusion. Les outils de pilotage ont été enrichis par de nouveaux tableaux de bord et des capacités d'export de données. Parallèlement, l'expérience utilisateur a été affinée via une meilleure visibilité des parcours (badges QPV, fins de contrat) et une gestion des accès renforcée. Ces évolutions sont soutenues par une montée en version technique majeure (Python 3.14) et une optimisation significative des processus de tests et de déploiement.

### Évolutions fonctionnelles
- **Parcours d'orientation** : Refonte complète du tunnel d'orientation et des pages de détails pour l'intégration de data·inclusion ; automatisation des notifications par email (rappels, acceptations, refus) et gestion intégrée des pièces jointes.
- **Suivi des usagers** : Ajout d'un onglet "Orientations" sur la fiche usager, affichage de badges de localisation (QPV) et meilleure visibilité des situations de fin de parcours et des fins de contrat imminentes.
- **Pilotage et statistiques** : Création d'un nouveau tableau de bord d'évaluation GEIQ, possibilité d'exporter les orientations et les services vers Metabase, et nouveaux indicateurs de comptage des employés en fin de parcours.
- **Recherche et interface** : Amélioration des formulaires de recherche en page d'accueil, mise à jour de la navigation (candidatures, orientations), harmonisation des icônes et passage de la liste des candidatures en vue tableau.
- **Gestion des comptes et accès** : Renforcement de l'usage de ProConnect pour le personnel, amélioration du processus de création/désactivation des comptes professionnels et blocage de la création de comptes en double.
- **Candidatures** : Amélioration du suivi des candidatures et possibilité de fermer un recrutement en cas de refus pour "absence de poste".

### Évolutions techniques
- **Core et Infrastructure** : Passage à Python 3.14, remplacement de MinIO par RustFS et ajout de Gunicorn pour la gestion du serveur.
- **Performance** : Optimisation des pages d'administration (pagination et hiérarchie des dates) et réduction du temps de configuration initiale du système.
- **CI/CD et Tests** : Accélération de la suite de tests via le partitionnement (sharding) en 4 flux, mise en cache des bibliothèques spatiales et amélioration globale de la stabilité et de la vitesse des tests.
- **Architecture et Sécurité** : Refonte du workflow de gestion des dossiers employés, nettoyage des composants obsolètes (Nexus, DORA) et renforcement de la traçabilité (audit trail) incluant les détails de connexion et de navigation.

### Autres changements
- **Documentation** : Ajout de la documentation concernant la piste d'audit (audit trail).
- **Maintenance** : Nettoyage du code mort, suppression de fichiers statiques inutilisés et mise à jour des configurations de domaine et de thèmes.
