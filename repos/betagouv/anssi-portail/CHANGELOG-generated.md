## Changelog : anssi-portail (30 derniers jours, au 04 septembre 2026)

### Résumé
Ce mois a été marqué par une transformation majeure de l'expérience utilisateur, avec le lancement de nouveaux contenus interactifs sous forme de "mini-tests" (quiz vrai/faux) et une refonte visuelle globale du portail. Parallèlement, une modernisation technique profonde a été opérée pour améliorer les performances et la maintenabilité de l'application.

### Évolutions fonctionnelles
- **Nouveaux Mini-tests :** Introduction de quiz interactifs de type "Vrai/Faux" incluant des animations (confettis), des écrans de succès/erreur, et la possibilité pour les utilisateurs de laisser des réactions.
- **Refonte de la Direction Artistique (DA) :** Mise à jour globale de l'identité visuelle avec de nouveaux motifs de fond, des illustrations animées, une nouvelle palette de couleurs et une typographie optimisée pour une meilleure lisibilité.
- **Amélioration du Parcours de Sécurisation :** 
    - Création de nouvelles pages d'accueil (landings) pour les parcours "basique" et "complet".
    - Ajout de fils d'Ariane pour faciliter la navigation.
    - Intégration de pictogrammes et d'animations pour illustrer les étapes.
- **Évolutions des Tests de Maturité :** Amélioration de l'affichage des résultats, ajout de nouveaux graphiques et mise en place d'un système de retour utilisateur (satisfaction) directement sur les pages de résultats.
- **Statistiques :** Enrichissement du tableau de bord des statistiques, incluant désormais le nombre de tests réalisés et les indicateurs de satisfaction utilisateur.

### Évolutions techniques
- **Migration Svelte 5 :** Migration massive de l'ensemble des composants du projet vers Svelte 5 (utilisation du mode "runes") pour optimiser la réactivité et les performances.
- **Suivi et Événements :** 
    - Intégration poussée de l'outil Brevo pour le suivi des événements (complétion de parcours, déblocage de badges).
    - Amélioration de la persistance du parcours utilisateur et de la mémorisation des campagnes d'origine.
- **Architecture API :** 
    - Création de nouvelles routes backend dédiées à la gestion des mini-tests (récupération des questions, soumission des réponses et gestion des réactions).
    - Refonte de l'API de statistiques pour une consommation plus efficace des données.
- **Développement :** Amélioration de l'environnement de développement local (support LAN, optimisation de la configuration Nix).

### Autres changements
- **Nettoyage du code :** Travail important de suppression des composants, styles CSS, images et dépendances inutilisés pour alléger l'application.
- **Documentation :** Mise à jour du guide de développement et des procédures d'exploitation.
- **Design System :** Mises à jour régulières du kit UI interne (`@lab-anssi/ui-kit`).
