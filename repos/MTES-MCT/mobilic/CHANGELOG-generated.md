## Changelog : mobilic (30 derniers jours, au 21/09/2026)

### Résumé
Ce mois-ci, Mobilic a renforcé ses capacités de suivi et d'alerte, notamment via l'introduction de nouveaux avertissements en temps réel pour les saisies et une meilleure visibilité des seuils de repos pour les gestionnaires. L'interface a été enrichie de nouvelles pages d'information et modernisée pour offrir une meilleure expérience utilisateur et une conformité accrue aux standards d'accessibilité.

### Évolutions fonctionnelles
- **Alertes et Notifications**
    - Mise en place de bannières d'alerte pour les saisies en temps réel, avec une gestion améliorée de l'empilement et la possibilité de les masquer [#964](https://github.com/MTES-MCT/mobilic/pull/964).
    - Introduction des notifications push pour améliorer le suivi des utilisateurs [#920](https://github.com/MTES-MCT/mobilic/pull/920).
    - Amélioration de la visibilité et de la mise en forme des barres de notification.
- **Interface Administrateur**
    - Ajout d'une colonne de repos et d'alertes de seuil dans les vues hebdomadaires et mensuelles pour faciliter le pilotage.
    - Amélioration de la gestion des employés (détection des utilisateurs inactifs, gestion des types de transport et d'activités).
    - Migration du menu latéral vers le composant SideMenu du DSFR [#953](https://github.com/MTES-MCT/mobilic/pull/953).
- **Nouvelles pages et contenus**
    - Ajout d'une page dédiée au schéma pluriannuel et mise à jour de la déclaration d'accessibilité.
    - Création d'une page "Partenaires" incluant le logo de Rota.
- **Expérience Utilisateur (PWA & Mobile)**
    - Optimisation du tunnel de création de mission, désormais accessible directement depuis le menu de navigation.
    - Correction de bugs critiques, notamment l'écran blanc au chargement de l'application [#926](https://github.com/MTES-MCT/mobilic/pull/926).
    - Correction des références légales concernant la définition de la semaine civile.
    - Amélioration de la précision des données d'historique et des labels d'activité.

### Évolutions techniques
- **Architecture et Refactoring**
    - Migration de la récupération des seuils hebdomadaires du client vers le backend pour garantir la cohérence des données.
    - Refactorisation de la gestion des types d'activités et du contexte d'actions pour une meilleure stabilité globale.
    - Nettoyage du code (suppression de code mort et de gardes inutilisées).
- **Accessibilité et Qualité**
    - Amélioration de l'accessibilité via l'utilisation de composants natifs et une structure DOM optimisée.
    - Résolution de nombreux avertissements et erreurs de linting sur l'ensemble du projet.
    - Amélioration de la capture d'erreurs Sentry concernant les jetons de rafraîchissement (refresh tokens).

### Autres changements
- Corrections de fautes de frappe sur la page d'accueil et les labels de l'interface.
- Ajustements cosmétiques du header et de la navigation.
