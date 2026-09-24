## Changelog : mobilic (30 derniers jours, au 23 septembre 2026)

### Résumé
Ce mois-ci, Mobilic a renforcé ses capacités de contrôle réglementaire et l'expérience utilisateur mobile. Les évolutions majeures concernent une meilleure précision du suivi des seuils de repos pour les administrateurs, l'introduction de nouvelles bannières d'alerte pour les employés (notamment sur la saisie en temps réel) et l'amélioration de l'accessibilité de la plateforme.

### Évolutions fonctionnelles
- **Alertes et notifications :** Mise en place de bannières d'alerte pour les employés (notamment pour signaler les saisies en temps réel) et déploiement des notifications push. [#920](https://github.com/MTES-MCT/mobilic/pull/920), [#964](https://github.com/MTES-MCT/mobilic/pull/964)
- **Gestion administrative :** Amélioration du suivi des seuils de repos hebdomadaires par employé et par type d'activité, avec l'ajout de colonnes de repos et d'alertes de seuil dans les vues hebdomadaires et mensuelles. [#934](https://github.com/MTES-MCT/mobilic/pull/934), [#965](https://github.com/MTES-MCT/mobilic/pull/965)
- **Nouvelles pages et contenus :** Ajout d'une page dédiée au schéma pluriannuel et intégration du logo Rota dans la section des partenaires. [#940](https://github.com/MTES-MCT/mobilic/pull/940), [#955](https://github.com/MTES-MCT/mobilic/pull/955)
- **Expérience mobile (PWA) :** Accès direct au tunnel de création de mission via le menu de navigation et corrections de l'affichage des boutons d'activité.
- **Gestion des utilisateurs :** Correction de l'affichage des employés inactifs dans le tableau de bord administrateur.

### Évolutions techniques
- **Refonte de l'interface :** Migration du menu latéral vers le composant SideMenu du Design System (DSFR). [#953](https://github.com/MTES-MCT/mobilic/pull/953)
- **Architecture et fiabilité :** Centralisation du `ActionsContext` pour une portée globale et migration de la gestion des seuils hebdomadaires du client vers le backend. [#949](https://github.com/MTES-MCT/mobilic/pull/949)
- **Maintenance et robustesse :** Résolution de problèmes de linting, correction de la gestion des tokens de rafraîchissement (Sentry) et unification des comportements entre le front et le back pour les options de mission. [#914](https://github.com/MTES-MCT/mobilic/pull/914)

### Autres changements
- **Accessibilité :** Mise à jour de la déclaration d'accessibilité et corrections typographiques sur les pages informatives.
- **Nettoyage :** Suppression de code mort et de garde inutilisés dans l'interface d'administration.
