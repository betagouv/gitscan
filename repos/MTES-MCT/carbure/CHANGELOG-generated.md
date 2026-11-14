## Changelog : carbure (30 derniers jours, au 02/11/2026)

### Résumé
Ce mois a été marqué par une refonte majeure du moteur de traçabilité, améliorant la précision des calculs grâce à une meilleure gestion des unités et des propriétés des matériaux. Le module biométhane a été considérablement enrichi avec un nouvel espace dédié aux fournisseurs de gaz et une gestion optimisée des réouvertures de déclarations. Enfin, l'expérience de gestion de l'hydrogène et de l'administration des utilisateurs a été simplifiée et affinée.

### Évolutions fonctionnelles
- **Biométhane** : 
    - Création d'un espace dédié pour les fournisseurs de gaz permettant de consulter les déclarations liées à leurs contrats.
    - Mise en place d'un processus de réouverture des déclarations annuelles avec notification automatique des producteurs.
    - Amélioration de la saisie des données (gestion des résidus IAA, affichage des labels et des unités).
- **Traçabilité** : 
    - Amélioration de la précision des mesures en permettant le choix entre masse, volume ou énergie, et en intégrant les propriétés physiques (PCI, densité) directement dans les actions.
    - Meilleure visibilité sur les périodes de travail et les filtres de statut.
- **Hydrogène** : 
    - Ajout de filtres par statut pour les lots d'hydrogène.
    - Partage de la vue des certificats entre les opérateurs et les administrateurs.
    - Amélioration de la recherche de lots par entreprise pour les administrateurs du secteur.
- **Administration & Gestion** : 
    - Optimisation de la gestion des utilisateurs et des entreprises (nouveaux tris, affichage des compteurs d'utilisateurs).
    - Affinement des règles d'affichage des types de livraison et d'usage pour les lots.
- **Bioéthanol** : Masquage (non suppression) des produits ETBE-100 et ETBE-63.

### Évolutions techniques
- **Moteur de traçabilité** : Refonte de l'architecture pour supporter une hiérarchie parent/enfant plus robuste et une gestion des transitions basée sur une matrice de statuts.
- **Gestion des données** : 
    - Automatisation de l'importation du catalogue de matériaux via des fichiers CSV.
    - Optimisation des imports Excel pour une meilleure gestion des facteurs de conversion des matériaux.
- **API & Sécurité** : 
    - Optimisation des performances de l'API via une sérialisation explicite des champs.
    - Correction de la gestion des certificats de sécurité (emSign).
    - Mise à jour des schémas OpenAPI pour le module biométhane.

### Autres changements
- **Nettoyage** : Extraction du module `EntityCertificate` pour une meilleure modularité.
- **Tests** : Amélioration de la couverture de tests sur les modules biométhane et hydrogène.
- **Configuration** : Utilisation de variables d'environnement pour la gestion des mots de passe lors des phases de seed.
