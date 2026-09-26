## Changelog : etape (30 derniers jours, au 24 septembre 2026)

### Résumé
Ce mois a été marqué par une refonte majeure de l'expérience utilisateur du simulateur, incluant une réécriture des règles métier et une nouvelle interface pour le questionnaire et les résultats. Parallèlement, la plateforme a franchi des étapes importantes de maturité technique avec la migration de son infrastructure de déploiement et la mise en place de standards de développement plus stricts.

### Évolutions fonctionnelles
- **Refonte du simulateur** : Révision complète du parcours de questionnement et de la page de résultats pour mieux correspondre aux règles métier ([#56](https://github.com/betagouv/etape/issues/56)).
- **Nouvelles fonctionnalités** :
    - Intégration de l'authentification via FranceConnect ([#16](https://github.com/betagouv/etape/issues/16)).
    - Possibilité de télécharger les résultats de la simulation au format PDF, avec des liens cliquables et une mise en page optimisée ([#49](https://github.com/betagouv/etape/issues/49)).
- **Améliorations de l'expérience utilisateur (UX/UI)** :
    - Optimisation du questionnaire : gestion de la barre de progression, meilleur positionnement des messages d'erreur, et comportement plus intuitif des boutons "Suivant" et "Précédent".
    - Affichage de l'ancienneté amélioré (format date) et simplification de l'écran de situation.
    - Correction de l'affichage des données dans les tableaux de rendu.
- **Contenu** : Mise à jour du glossaire (ajout des notions de brouillon, accusé et historique) et bascule vers le service du portail CEP national.

### Évolutions techniques
- **Backend & Architecture** :
    - Migration de NestJS de la version 11 vers la version 12.
    - Refactorisation de l'API avec une séparation plus nette des couches et adoption de TanStack Query.
    - Mise en place de contrats de routes partagés.
- **Infrastructure & CI/CD** :
    - Migration du système de déploiement : abandon de Vercel au profit d'un nouveau circuit basé sur des machines virtuelles gérées via Ansible.
    - Automatisation du déploiement sur l'environnement de développement à chaque fusion sur la branche principale.
    - Renforcement de la chaîne de tests avec l'ajout de tests de bout en bout pour le registre Harbor ([#57](https://github.com/betagouv/etape/issues/57)).
    - Intégration d'outils de suivi (Matomo et Sentry).
- **Qualité du code** :
    - Instauration de nouvelles conventions de nommage (français/anglais) et de règles de typage strictes.
    - Mise en place d'outils de revue automatique pour les pratiques React et l'accessibilité.

### Autres changements
- **Documentation** : Mise à jour massive de la documentation technique (stack front-end, pratiques React, procédures d'infrastructure Ansible et guides d'accessibilité).
- **Nettoyage** : Correction de nombreux écarts de nommage et alignement avec le Design System.
