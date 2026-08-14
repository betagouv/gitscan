## Changelog : egapro (30 derniers jours, au 13 août 2026)

### Résumé
Ce mois a été marqué par un effort important de refonte visuelle et d'amélioration de l'expérience utilisateur, notamment pour la déclaration de la rémunération et l'édition des documents PDF. La plateforme gagne en fiabilité grâce à une meilleure intégration des données de l'effectif (GIP) et à un renforcement massif de l'accessibilité (RGAA) et des tests automatisés.

### Évolutions fonctionnelles

**Design et Interface Utilisateur**
- Refonte complète du design de la déclaration de rémunération (pages 1 à 5) et du template PDF de déclaration pour correspondre aux nouvelles maquettes [#3935](https://github.com/SocialGouv/egapro/issues/3935), [#3973](https://github.com/SocialGouv/egapro/issues/3973).
- Alignement général de l'interface (tuiles, cartes, formulaires, fil d'Ariane) sur les maquettes Figma pour une cohérence visuelle accrue [#4147](https://github.com/SocialGouv/egapro/issues/4147), [#4143](https://github.com/SocialGouv/egapro/issues/4143), [#4134](https://github.com/SocialGouv/egapro/issues/4134).
- Amélioration de la lisibilité des indicateurs (gestion des décimales, seuils symétriques et masquage de l'effectif exact sous certains paliers) [#4039](https://github.com/SocialGouv/egapro/issues/4039), [#4040](https://github.com/SocialGouv/egapro/issues/4040), [#4149](https://github.com/SocialGouv/egapro/issues/4149).

**Parcours et Règles Métier**
- Ajout de nouveaux éléments de navigation : bouton "Je donne mon avis" en fin de parcours [#3966](https://github.com/SocialGouv/egapro/issues/3966) et affichage immédiat du récapitulatif après la soumission [#4130](https://github.com/SocialGouv/egapro/issues/4130).
- Renforcement des contrôles de saisie : blocage de l'accès au tunnel de déclaration si les informations obligatoires (téléphone ou CSE) sont manquantes [#4117](https://github.com/SocialGouv/egapro/issues/4117).
- Correction de parcours critiques, notamment la résolution d'une boucle de redirection infinie sur la section avis du CSE [#4061](https://github.com/SocialGouv/egapro/issues/4061).

**Fiabilité des Données**
- Amélioration de la précision des calculs : les effectifs et les écarts (A-D) sont désormais prioritairement récupérés depuis le GIP plutôt que recalculés localement, garantissant une cohérence des données [#4121](https://github.com/SocialGouv/egapro/issues/4121), [#4104](https://github.com/SocialGouv/egapro/issues/4104), [#3962](https://github.com/SocialGouv/egapro/issues/3962).

### Évolutions techniques

**Accessibilité**
- Mise en place d'un système d'accessibilité global (ultra11y) et réalisation d'un lot important de remédiations pour la conformité RGAA [#3887](https://github.com/SocialGouv/egapro/issues/3887), [#3889](https://github.com/SocialGouv/egapro/issues/3889).

**Qualité et Tests**
- Extension de la couverture de tests de bout en bout (E2E) pour couvrir l'intégralité des parcours utilisateurs [#4097](https://github.com/SocialGouv/egapro/issues/4097).
- Rationalisation de la suite de tests E2E pour se concentrer sur les chemins critiques et améliorer la vitesse d'exécution [#3928](https://github.com/SocialGouv/egapro/issues/3928).

**Infrastructure et CI/CD**
- Optimisation des pipelines de déploiement, incluant la gestion d'environnements de test persistants et le versionnement automatique des images [#3904](https://github.com/SocialGouv/egapro/issues/3904), [#4057](https://github.com/SocialGouv/egapro/issues/4057).
- Amélioration de la sécurité des communications via l'implémentation du certificat client mTLS pour les appels vers le service SUIT [#4101](https://github.com/SocialGouv/egapro/issues/4101).
- Refactorisation du moteur de gestion des étapes (FSM) pour une meilleure robustesse du code [#3979](https://github.com/SocialGouv/egapro/issues/3979).

### Autres changements
- Mise à jour de la version du projet affichée dans le pied de page [#4139](https://github.com/SocialGouv/egapro/issues/4139).
- Amélioration de la documentation technique et des processus de release via l'intégration d'outils d'IA [#4046](https://github.com/SocialGouv/egapro/issues/4046).
