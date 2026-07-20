## Changelog : seves (30 derniers jours, au 2026-07-16)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'expérience utilisateur, notamment dans les formulaires de conclusion et de recherche, avec l'introduction de nouveaux composants interactifs comme Treeselect. Des corrections de bugs et des améliorations de la sécurité ont également été apportées, ainsi qu'une documentation de l'architecture du projet.

### Évolutions fonctionnelles
- **Conclusions :**
    - Possibilité de supprimer une conclusion. [#issue](lien vers issue si disponible)
    - Pré-remplissage amélioré des formulaires de conclusion pour les repas, les aliments suspects et les établissements.
    - Déplacement du formulaire de conclusion dans une modale pour une meilleure expérience utilisateur.
    - Correction de bugs liés à l'édition et à la suppression des conclusions.
- **Filtres et recherches :**
    - Introduction de Treeselect pour les filtres de sources et types SSA, SV et TIAC, offrant une sélection multiple plus intuitive. [#issue](lien vers issue si disponible)
    - Possibilité de filtrer par plusieurs structures et contacts.
    - Amélioration de la sélection des dangers pour TIAC.
- **Notifications :**
    - Envoi de notifications DI aux agents.
- **Autres améliorations UI/UX :**
    - Amélioration de la gestion des valeurs lors de la fermeture des modales Lieu et Repas.
    - Correction de l'affichage des dates dans la liste des révisions.
    - Harmonisation de la terminologie de navigation pour SV.
    - Correction de problèmes d'affichage et de comportement des boutons dans les modales.
    - Ajout de l'Organisme nuisible.

### Évolutions techniques
- **Architecture :** Ajout de la documentation de l'architecture du projet.
- **Sécurité :**
    - Amélioration de la sécurité des vues TIAC.
    - Précision de la politique de sécurité du contenu (CSP).
    - Exclusion des membres de l'équipe SEVES de la désactivation de compte.
- **Tests :**
    - Amélioration et stabilisation des tests pour les messages SV, les conclusions et TIAC.
    - Correction de tests pour les documents.
- **Déploiement :**
    - Optimisation du nombre de workers en CI.

### Autres changements
- Mise à jour de plusieurs dépendances : Django, Django-filter, sentry-sdk, pytest-rerunfailures, ruff, playwright, redis, django-debug-toolbar, django-environ, soupsieve, django-reversion-compare. (Ces mises à jour de routine ont été omises dans le détail, mais sont incluses ici pour information).
