## Changelog : anssi-portail (30 derniers jours, au 30 octobre 2026)

### Résumé
Ce mois a été marqué par une montée en puissance majeure des outils interactifs. Le simulateur de hameçonnage est désormais pleinement opérationnel avec de nombreux scénarios réalistes et un système de correction immédiate. La boîte à outils s'est considérablement enrichie de nouveaux modèles de documents et d'un système de collecte d'avis utilisateurs, tandis que les parcours de sécurisation sont désormais intégrés de manière fluide à travers tout le portail pour mieux guider les utilisateurs.

### Évolutions fonctionnelles
- **Simulateur de hameçonnage** : 
    - Ajout de nombreux scénarios d'emails (ANSSI, Banque Postale, Orange, La Poste, CPF, Inpi, ProConnect) incluant leurs réponses types.
    - Amélioration de l'expérience utilisateur avec un retour visuel immédiat (bonne/mauvaise réponse), la distinction des messages lus et une interface entièrement adaptée aux mobiles et tablettes.
- **Boîte à outils** : 
    - Ajout de nouveaux modèles de documents (revue des droits d'accès, revue de comptes utilisateurs, modification de mots de passe, liste d'activités, annuaire de crise).
    - Mise en place d'un système de retours utilisateurs permettant de noter les outils et de soumettre des commentaires directement depuis l'interface.
- **Parcours de sécurisation** : Intégration visuelle et fonctionnelle des parcours dans les zones clés du site (page d'accueil, résultats de tests, scores de maturité et pied de page) pour un accompagnement personnalisé.
- **Blog & Contacts** : 
    - Déploiement de la section blog avec gestion des articles et des retours utilisateurs.
    - Enrichissement de l'annuaire de contacts avec l'ajout de données nationales, régionales et sectorielles.

### Évolutions techniques
- **Architecture & API** : 
    - Réorganisation complète des routes API (outils, annuaires, authentification, mini-tests) pour une meilleure structure.
    - Centralisation de la gestion des états (emails, outils) via un store pour plus de cohérence.
- **Infrastructure & Toolchain** : 
    - Migration de la stack vers Node.js 26.
    - Mise à jour de l'environnement Ruby et optimisation de la configuration Svelte (hot reload, chargement des chunks).
- **Frontend** : 
    - Refactorisation du simulateur de hameçonnage en composants réutilisables.
    - Adoption accrue des composants du Design System (DSFR) pour les alertes et les notifications.
- **Performance & Robustesse** : 
    - Implémentation du cache pour les articles du blog.
    - Amélioration de la gestion des erreurs avec un composant 404 réutilisable.

### Autres changements
- **SEO & Visibilité** : Optimisation des métadonnées (titres, descriptions, réseaux sociaux) et intégration des articles du blog dans le sitemap.
- **Maintenance** : Nettoyage des dépendances obsolètes, suppression des commentaires inutiles et harmonisation du nommage des fichiers et variables.
