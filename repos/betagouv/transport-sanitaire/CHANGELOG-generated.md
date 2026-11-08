## Changelog : transport-sanitaire (30 derniers jours, au 4 novembre 2026)

### Résumé
Ce mois-ci a été marqué par une montée en version majeure avec l'intégration du modèle de règles v10. Le simulateur est devenu plus précis et robuste, offrant une interface utilisateur plus intuitive et une génération de documents (Cerfa, fiches patients) plus complète et mieux mise en page.

### Évolutions fonctionnelles
- **Intégration du modèle v10** : Mise à jour progressive du moteur de règles jusqu'à la version 10.1.6 [#338].
- **Gestion documentaire** : 
    - Génération et téléchargement des fiches patients et des formulaires Cerfa [#234, #107, #211].
    - Amélioration de la qualité des PDF (aplatissement des fichiers, gestion automatique de la taille du texte pour éviter les débordements) [#231, #108, #232].
- **Expérience utilisateur (UI/UX)** :
    - Interface modernisée : présentation des choix sous forme de cartes [#210] et affichage d'aides contextuelles sous les options [#232].
    - Aide à la saisie : rappel des données déjà renseignées pour éclairer les questions suivantes [#232] et affichage de données fixées à proximité des champs concernés [#232].
    - Nouvelles options : possibilité d'indiquer son établissement ou sa structure [#339] et invitation à laisser un avis après le résultat [#237].
- **Logique de simulation** : Prise en compte de parcours spécifiques (ALD, transports en avion ou bateau) [#226] et gestion intelligente du saut de questions sans effet sur le résultat [#263].
- **Suivi** : Envoi des verdicts de parcours ALD vers Matomo pour analyse [#269].

### Évolutions techniques
- **Refonte de l'architecture** : 
    - Restructuration profonde du "socle" (moteur) pour mieux séparer la définition des questions de leur exécution [#250].
    - Déplacement de la logique métier dans un répertoire `core/` dédié pour une meilleure organisation [#216].
- **Moteur de décision** : Intégration de Publicodes et compilation du graphe de décision directement lors de l'étape de build [#257].
- **Qualité et Tests** : Augmentation significative de la couverture de tests, incluant les scénarios de recette (N2, N4) et les cas d'usage de l'éditeur pour garantir la fiabilité des calculs [#314, #313, #293].
- **Outils de développement** : Amélioration de la CLI pour permettre le suivi de l'avancement des chantiers via GitHub Projects [#105].

### Autres changements
- **Documentation** : Mise à jour du glossaire et des documents techniques relatifs aux capacités du socle et au nouveau modèle v10 [#238, #239].
- **Maintenance** : Renommage officiel du dépôt en `transport-sanitaire` [#217].
