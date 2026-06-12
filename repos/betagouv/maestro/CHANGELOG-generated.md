## Changelog : maestro (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, l'équipe de Maestro a déployé de nombreuses améliorations, notamment autour de la gestion des laboratoires, des prélèvements et des analyses. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur. L'application continue d'évoluer pour répondre aux besoins des agents de l'administration dans la gestion des données environnementales et sanitaires.

### Évolutions fonctionnelles
- Ajout d'une interface pour configurer les laboratoires et leurs analytes [#920].
- Possibilité de filtrer les prélèvements par département pour les administrations centrales [#3c18a93].
- Amélioration de la gestion des documents pour le suivi national, permettant le dépôt de documents [#1051].
- Ajout d'une API dédiée à SEVES [#80ef3c1].
- Gestion des agréments des laboratoires dans LabCam [#8c49371].
- Possibilité d'imprimer le formulaire vierge pour les DAOA après sélection de l'abattoir [#c71d3d9].
- Amélioration de la gestion des LMR (Limites Maximales de Résidus) avec prise en compte de certaines LMR optionnelles [#616abbd].
- Ajout de la date de création des utilisateurs dans Maestro [#80ef3c1].
- Correction de l'affichage du tableau de bord lorsqu'il n'y a pas d'actions prioritaires [#1054].
- Correction de la réinitialisation de la modale de recevabilité [#6d6890b].
- Correction de l'affichage du numéro DAP et du code barre échantillon [#7a57781].
- Correction de la gestion des statuts suite à l'analyse des échantillons [#a137db9].

### Évolutions techniques
- Amélioration du typage des réponses de l'API [#b78df31].
- Refactorisation de l'URL avec un builder typé [#c5f03d8].
- Remplacement de `swc` par `node` pour certaines tâches [#ab687ee].
- Utilisation d'une meilleure méthode pour ajouter des pièces jointes avec Nodemailer [#78c1a30].
- Mise à jour de nombreuses dépendances (voir section "Autres changements").
- Correction d'un problème de capture des erreurs `console.error` avec Sentry (puis rétractation de la correction en raison de problèmes) [#5a11e34, #69c611e].
- Ajout d'alertes Mattermost en cas d'échec d'envoi d'emails via Brevo [#1cbe5f4].

### Autres changements
- Mise à jour de plusieurs dépendances : `@aws-sdk/client-s3`, `i18next`, `shell-quote`, `actions/checkout`, `github/codeql-action`, `@biomejs/biome`, `vite`, `@types/react`, `@reduxjs/toolkit`, `lefthook`, `date-fns`, `puppeteer-core`, `playwright`, `@types/node`, `@mui/material`, `@aws-sdk/s3-request-presigner`, `fast-xml-builder`, `react-dom`, `react-router`, `fast-xml-parser`, et d'autres.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Nettoyage du code et refactoring de certains composants.
- Correction de quelques balises dans l'interface utilisateur [#8d17f9a].
- Ajout de l'identifiant de l'acteur dans Sacha [#d80f2a4].
- Correction du filtre sur les `programmingPlanKinds` dans la gestion des utilisateurs [#aaaea64].
- Correction d'un problème avec les réponses non définies dans Zod [#6f2750a].
- Correction de l'extraction du numéro d'exemplaire dans PPV [#6e4a42d].
- Correction de la duplication de la date du prélèvement [#e47a28a].
- Correction de l'association du prélèvement à sa programmation [#347ca75].
- Correction de l'export des prélèvements par année [#cc522ab].
- Correction de la gestion de la conformité des prélèvements [#821fe0d].
- Correction de l'ajout des types de ressources réglementation et modèle [#ea86394].
- Suppression des utilisateurs non actifs de la liste des préleveurs [#476dd7c].
- Correction de l'ajout de préfixes aux destinataires dans Sacha [#5a7f594].
- Correction de l'utilisation du relai SMTP Brevo pour l'envoi d'emails [#2834570].
- Passage de GPG en mode non interactif [#39733a5].
- Ajout d'un utilitaire typé pour la gestion du menu [#463b63e].
- Transformation des onglets du menu d'administration en liens [#e35885f].
- Ajout de la prise en compte des non quantifiables pour Cereco [#90c424c].
- Correction du nouveau nom de colonne dans Cereco [#5723d7c].
- Correction de l'interprétation des nouvelles syntaxes LMR par Inovalys [#855339b, #b2b8b39].
- Correction de l'email contenu dans la clé GPG [#81cf0f5].
