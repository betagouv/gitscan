## Changelog : les-emplois (30 derniers jours, au 26 octobre 2026)

### Résumé
Ce mois a été marqué par une refonte majeure du parcours d'orientation pour intégrer les besoins de "data·inclusion", incluant de nouvelles fonctionnalités pour les prestataires de services et l'automatisation des notifications par email. L'expérience utilisateur a été affinée avec un changement de terminologie (passage de "candidat" à "usager") et une interface plus intuitive. Enfin, des optimisations de performance significatives et une mise à jour majeure de l'environnement technique (Python 3.14) ont été réalisées pour garantir la stabilité et la rapidité du service.

### Évolutions fonctionnelles
- **Orientation et Insertion :** 
    - Refonte complète du parcours d'orientation (wizard, pages de détails des services et des structures) pour l'intégration de "data·inclusion".
    - Les prestataires de services peuvent désormais accepter ou décliner les orientations reçues.
    - Automatisation des notifications par email pour le suivi des orientations (création, acceptation, refus, expiration).
    - Ajout de nouveaux champs et de la possibilité de s'inscrire à des événements de mobilisation.
- **Expérience Utilisateur (UX/UI) :** 
    - Harmonisation de la terminologie sur l'ensemble de la plateforme (utilisation de "usager" au lieu de "candidat").
    - Amélioration de la navigation via l'ajout d'onglets dédiés (orientations, candidatures) sur les profils.
    - Ajout de nouveaux indicateurs visuels et badges (zones QPV, disponibilité des postes, fin de parcours).
    - Amélioration des formulaires de recherche et de la cohérence des menus.
- **Gestion des Utilisateurs et Accès :** 
    - Amélioration du processus de gestion des comptes (désactivation, réactivation et création de nouveaux comptes pour les professionnels).
    - Renforcement de la sécurité et de la fluidité des connexions via ProConnect.
    - Mise en place de restrictions pour empêcher la création de comptes en doublon ou le partage d'approbations entre plusieurs usagers.
- **Pilotage et Administration :** 
    - Création d'un nouveau tableau de bord pour l'évaluation des bilans GEIQ.
    - Exportation des données d'orientation et de services vers Metabase pour un meilleur suivi statistique.
    - Ajout de vues de listes pour les organisations et amélioration de l'affichage des contrats dans l'administration.

### Évolutions techniques
- **Infrastructure et Core :** 
    - Migration vers Python 3.14.
    - Remplacement de MinIO par RustFS pour la gestion du stockage.
- **Performance :** 
    - Optimisation de l'interface d'administration Django (utilisation de paginateurs et de hiérarchies de dates plus performants sur les grandes tables).
    - Réduction du temps de résolution d'URL lors de l'initialisation du service.
- **CI/CD et Tests :** 
    - Mise en place du partitionnement des tests (sharding) pour accélérer les cycles de validation.
    - Optimisation du cache pour les bibliothèques spatiales dans la CI.
    - Amélioration de la stabilité et de la vitesse de la suite de tests.
- **Sécurité et Traçabilité :** 
    - Enrichissement de la piste d'audit (suivi du navigateur et des détails de connexion ProConnect).
    - Amélioration de l'extraction des adresses IP pour la limitation de débit (rate-limiting).
- **Refactoring :** 
    - Nettoyage du composant Nexus et suppression de code mort.
    - Refonte de la gestion des statuts et des transitions de workflow pour les dossiers employés.

### Autres changements
- **Maintenance et Nettoyage :** 
    - Suppression de fichiers statiques et de styles CSS inutilisés.
    - Mise à jour des modèles d'emails, des signatures et des templates de communication.
    - Mise à jour de la documentation technique et des commentaires de code.
