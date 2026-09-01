## Changelog : les-emplois (30 derniers jours, au 31 août 2026)

### Résumé
Ce mois a été marqué par le déploiement majeur du module de gestion des orientations (Insertion), permettant un suivi plus fin des parcours. Le projet a également progressé sur l'amélioration de l'accompagnement des candidats (nouveaux onglets et fonctionnalités pour les conseillers) et sur le renforcement des outils de pilotage via de nouveaux tableaux de bord analytiques (Metabase/GEIQ).

### Évolutions fonctionnelles
- **Gestion des orientations (Insertion) :**
    - Mise en place d'un module complet pour visualiser les détails d'une orientation et gérer les pièces jointes.
    - Ajout de filtres avancés pour les listes d'orientations (par bénéficiaire, structure, expéditeur ou statut).
    - Automatisation de la synchronisation des statuts d'orientation.
- **Accompagnement et suivi des candidats :**
    - Création d'un onglet "Accompagnateurs" dans la vue des chercheurs d'emploi pour un meilleur suivi.
    - Possibilité pour les prescripteurs de demander une revue d'accompagnement auprès des SIAE.
    - Amélioration de la gestion des affectations : fin automatique des anciennes affectations et gestion des modes d'affichage.
    - Obligation de saisir un commentaire lors du report d'une candidature.
- **Interface et expérience utilisateur :**
    - Ajout de bannières d'alerte pour les webinaires thématiques sur le tableau de bord.
    - Intégration d'une carte "Mon Récap" pour les services partenaires.
    - Amélioration des filtres de recherche (notamment sur le handicap et les critères GEIQ/OPCS).
- **Administration :**
    - Possibilité pour le support de générer des liens de prolongation hors délais.
    - Autorisation pour le groupe "itou-admin" de commenter les dossiers de candidature annulés.

### Évolutions techniques
- **Données et Pilotage :**
    - Création de nouvelles tables pour alimenter les tableaux de bord Metabase dédiés au GEIQ.
    - Enrichissement des données analytiques avec l'ajout d'identifiants uniques (UID) pour les entreprises, prescripteurs, chercheurs d'emploi et utilisateurs.
- **Sécurité et Authentification :**
    - Amélioration de la gestion de la double authentification (MFA/TOTP) dans l'interface d'administration.
    - Optimisation des scopes utilisés pour l'API France Travail afin de respecter le principe de moindre privilège.
    - Renforcement de la sécurité lors de l'utilisation des codes de récupération OTP.
- **Performance et Architecture :**
    - Optimisation des requêtes SQL dans les vues des chercheurs d'emploi pour améliorer la rapidité d'affichage.
    - Refactorisation de la logique de validation des critères certifiés (niveaux 1 et 2).
    - Réduction du nombre d'appels inutiles dans les templates pour optimiser le rendu des pages.
- **CI/CD et Infrastructure :**
    - Amélioration des workflows CI (formatage et possibilité de déclenchement manuel).
    - Documentation de l'alternative Podman pour l'usage de conteneurs sur Debian.

### Autres changements
- **Corrections diverses :** Résolution de nombreuses coquilles (typos) dans l'interface et les messages système.
- **Maintenance :** Mise à jour du thème graphique et nettoyage de code (suppression de variables et de tests obsolètes).
